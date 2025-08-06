# 🏞️ CitizenAP UI – Citizen Aqua Probe

Embedded system for real-time multiparametric water quality monitoring. Developed for **Raspberry Pi OS**, it runs as a **UI layer over the operating system**, enabling sensor management and communication with the Citizen Aqua Probe mobile app via **WiFi and Bluetooth Low Energy (BLE)**.  

## 🚀 Features  

✅ **Graphical User Interface (GUI):** Built with **PySide2**, it starts automatically when the Raspberry Pi is powered on.  
✅ **WiFi network management:** Handles networks using `wpa_cli`.  
✅ **Bluetooth Low Energy (BLE):** Communication with the CORPWATER app.  
✅ **Sensor management:** Supports **pH, temperature, dissolved oxygen (DO), turbidity, electrical conductivity (EC)** via an **ADC**.  
✅ **GPS module:** Captures and stores georeferenced location data.  
✅ **Integrated buttons:** Uses a **PCF8574** for reading physical buttons.  
✅ **Local database:** Stores data using **SQLite**.  

---

## 🔌 Protocols & Connectivity  

### 📱 **WiFi**  
- Managed via `wpa_cli` for network configuration without a terminal interface.  

### 🔵 **Bluetooth Low Energy (BLE)**  
- Used for communication with the Citizen Aqua Probe mobile app.  

### 📌 **GPS**  
- Uses the GPS module to capture measurement locations.  

### 📝 **Supported Sensors**  
| Sensor | Measurement | Interface |
|--------|------------|-----------|
| pH | Hydrogen potential | ADC |
| Temperature | °C | OneWire |
| Dissolved Oxygen (DO) | mg/L | ADC |
| Turbidity | NTU | ADC |
| Electrical Conductivity (EC) | µS/cm | ADC |

### 🎹 **Button Interface**  
- Managed using a **PCF8574** for reading physical button presses.  

---
