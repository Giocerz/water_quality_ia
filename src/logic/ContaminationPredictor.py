import os
import time
import json
import numpy as np

try:
    import tflite_runtime.interpreter as tflite
except ImportError:
    tflite = None
    print("tflite_runtime is not installed. Prediction will not work.")


def escalar_manual(x, params):
    x = np.asarray(x, dtype=np.float32)
    data_min = np.asarray(params["data_min_"], dtype=np.float32)
    data_range = np.asarray(params["data_range_"], dtype=np.float32)
    return (x - data_min) / data_range


class ContaminationPredictor:
    def __init__(
        self,
        scaler_path='./src/resources/ia_models/minmax_scaler_big.json',
        model_path='./src/resources/ia_models/model_big.tflite'
    ):
        self.scaler = None
        self.interpreter = None
        self.input_index = None
        self.output_index = None
        self.model_path = model_path
        self.scaler_path = scaler_path

        if tflite:
            self._load_scaler()
            self._load_model()

    def _load_scaler(self):
        if os.path.exists(self.scaler_path):
            with open(self.scaler_path, 'r') as f:
                self.scaler = json.load(f)
        else:
            print(f"Scaler JSON not found at: {self.scaler_path}")

    def _load_model(self):
        if os.path.exists(self.model_path):
            self.interpreter = tflite.Interpreter(model_path=self.model_path)
            self.interpreter.allocate_tensors()
            self.input_index = self.interpreter.get_input_details()[0]['index']
            self.output_index = self.interpreter.get_output_details()[0]['index']
        else:
            print(f"TFLite model not found at: {self.model_path}")

    def is_ready(self):
        """Check if the interpreter and scaler are loaded and tflite is available."""
        return tflite is not None and self.scaler is not None and self.interpreter is not None

    def predict(self, ph, od_percent, temp, ec):
        if not self.is_ready():
            print("System is not ready for prediction.")
            return None

        # Feature engineering
        features = {
            'Temp': temp,
            'OD%': od_percent,
            'PH': ph,
            'EC': ec,
            'Temp2': temp ** 2,
            'Temp_inv': 1 / temp if temp != 0 else 0,
            'CE2': ec ** 2,
            'pH2': ph ** 2,
            'pH_inv': 1 / ph if ph != 0 else 0,
            'log_TEMP': np.log(temp) if temp > 0 else 0,
            'log_CE': np.log(ec) if ec > 0 else 0,
            'log_pH': np.log(ph) if ph > 0 else 0,
            'Temp_x_pH': temp * ph,
            'pH_x_CE': ph * ec,
            'Temp_x_CE': temp * ec
        }

        columns = [
            'Temp', 'OD%', 'PH', 'EC',
            'Temp2', 'Temp_inv',
            'CE2', 'pH2', 'pH_inv',
            'log_TEMP', 'log_CE', 'log_pH',
            'Temp_x_pH', 'pH_x_CE', 'Temp_x_CE'
        ]

        input_vector = np.array([[features[col] for col in columns]], dtype=np.float32)
        scaled_input = escalar_manual(input_vector, self.scaler).astype(np.float32)

        # Run inference and time it
        start = time.time()
        self.interpreter.set_tensor(self.input_index, scaled_input)
        self.interpreter.invoke()
        output = self.interpreter.get_tensor(self.output_index)
        duration = time.time() - start

        # Binary classification
        if output.shape[1] == 1:
            probability = float(output[0][0])
            predicted_class = int(probability > 0.5)
        else:
            probabilities = output[0]
            predicted_class = int(np.argmax(probabilities))
            probability = float(probabilities[predicted_class])

        return {
            'prediction': predicted_class,
            'probability': round(probability, 4),
            'prediction_time_seconds': round(duration, 6)
        }
