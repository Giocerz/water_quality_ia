from PySide2.QtWidgets import QWidget
from PySide2.QtCore import QTimer
from src.views.ui_Keyboard import Ui_Form as Standard_Keyboard
from src.views.ui_NumericKeyboard import Ui_Form as Numeric_Keyboard

class KeyboardWidget(QWidget):
    def __init__(self, focusLine):
        QWidget.__init__(self)
        self.__ui = Standard_Keyboard()
        self.__ui.setupUi(self)
        self.__focusLine = focusLine 
        self.__focusLine.setFocus() 

        self.__capStatus = False 
        self.__numbersCharsStatus = False 
        self.__numberCharsStatus_2 = False 

        self.__timerBackSpace = QTimer(self)
        self.__timerBackSpace.setInterval(1000)
        self.__timerBackSpace.setSingleShot(True)
        self.__timerBackSpace.timeout.connect(self.__backspaceHeld)

        self.__set_minus()

        #Eventos al presionar
        buttons = [
            self.__ui.btn1, self.__ui.btn2, self.__ui.btn3, self.__ui.btn4, self.__ui.btn5, 
            self.__ui.btn6, self.__ui.btn7, self.__ui.btn8, self.__ui.btn9, self.__ui.btn10,
            self.__ui.btn11, self.__ui.btn12, self.__ui.btn13, self.__ui.btn14, self.__ui.btn15,
            self.__ui.btn16, self.__ui.btn17, self.__ui.btn18, self.__ui.btn19, self.__ui.btn20,
            self.__ui.btn22, self.__ui.btn23, self.__ui.btn24, self.__ui.btn25, self.__ui.btn26,
            self.__ui.btn27, self.__ui.btn28, self.__ui.btn31, self.__ui.btn32, self.__ui.btn34
        ]

        for button in buttons:
            button.clicked.connect(self.__btnClicked)


        self.__ui.btn21.clicked.connect(self.__capClicked)  # Capitalize
        self.__ui.btn30.clicked.connect(self.__numbersCharsClicked)  # Números y caracteres

        self.__ui.btn29.pressed.connect(self.__backspacePressed)  # Backspace
        self.__ui.btn29.released.connect(self.__backspaceReleased)  # Backspace

        self.__ui.btn33.setText(" ")
        self.__ui.btn33.clicked.connect(self.__btnClickedSpace)  # Espacio


    def changeFocusKeyboard(self, focus):
        self.__focusLine = focus
        self.__focusLine.setFocus()

    def __btnClicked(self):
        button = self.sender()
        buttonText = button.text()
        self.__focusLine.setText(self.__focusLine.text() + buttonText)
        self.__focusLine.setFocus()   

    def __btnClickedSpace(self):
        button = self.sender()
        buttonText = button.text()
        self.originalSize = button.size()
        self.__focusLine.setText(self.__focusLine.text() + buttonText)
        self.__focusLine.setFocus()   

    def __backspacePressed(self):
        self.__timerBackSpace.start()
        button = self.sender()
        self.__focusLine.setText(self.__focusLine.text()[:-1])
        self.__focusLine.setFocus()   
        
    def __backspaceReleased(self):
        self.__timerBackSpace.stop()
        self.__focusLine.setFocus()   

    def __backspaceHeld(self):
        self.__focusLine.clear()
        self.__focusLine.setFocus()    

    def __capClicked(self):
        if not self.__numbersCharsStatus:
            if not self.__capStatus:
                self.__capStatus = True #atributo booleano para conocer si el boton cap fue presionado
                self.__set_mayus()
            
            else:
                self.__capStatus = False #atributo booleano para conocer si el boton cap fue presionado
                self.__set_minus()

        else:
            if not self.__numberCharsStatus_2:
                self.__numberCharsStatus_2 = True

                self.__ui.btn21.setText("?123")

                self.__ui.btn1.setText('~')
                self.__ui.btn2.setText("´")
                self.__ui.btn3.setText('|')
                self.__ui.btn4.setText('•')
                self.__ui.btn5.setText('√')
                self.__ui.btn6.setText('π')
                self.__ui.btn7.setText('÷')
                self.__ui.btn8.setText('×')
                self.__ui.btn9.setText('¶')
                self.__ui.btn10.setText('∆')
                self.__ui.btn11.setText('£')
                self.__ui.btn12.setText('¢')
                self.__ui.btn13.setText('€')
                self.__ui.btn14.setText('¥')
                self.__ui.btn15.setText('^')
                self.__ui.btn16.setText('°')
                self.__ui.btn17.setText('=')
                self.__ui.btn18.setText('{')
                self.__ui.btn19.setText('}')
                self.__ui.btn20.setText("\\")

                self.__ui.btn22.setText('%')
                self.__ui.btn23.setText('©')
                self.__ui.btn24.setText("®")
                self.__ui.btn25.setText('™')
                self.__ui.btn26.setText('✓')
                self.__ui.btn27.setText('[')
                self.__ui.btn28.setText(']')


            else:
                self.__numberCharsStatus_2 = False

                self.__ui.btn21.setText("=\\<")

                self.__ui.btn1.setText('1')
                self.__ui.btn2.setText('2')
                self.__ui.btn3.setText('3')
                self.__ui.btn4.setText('4')
                self.__ui.btn5.setText('5')
                self.__ui.btn6.setText('6')
                self.__ui.btn7.setText('7')
                self.__ui.btn8.setText('8')
                self.__ui.btn9.setText('9')
                self.__ui.btn10.setText('0')
                self.__ui.btn11.setText('@')
                self.__ui.btn12.setText('#')
                self.__ui.btn13.setText('$')
                self.__ui.btn14.setText('_')
                self.__ui.btn15.setText('&')
                self.__ui.btn16.setText('-')
                self.__ui.btn17.setText('+')
                self.__ui.btn18.setText('(')
                self.__ui.btn19.setText(')')
                self.__ui.btn20.setText('/')

                self.__ui.btn22.setText('*')
                self.__ui.btn23.setText('"')
                self.__ui.btn24.setText("'")
                self.__ui.btn25.setText(':')
                self.__ui.btn26.setText(';')
                self.__ui.btn27.setText('!')
                self.__ui.btn28.setText('?')
        self.__focusLine.setFocus()   

    def __numbersCharsClicked(self):
        if not self.__numbersCharsStatus:
            self.__numbersCharsStatus = True #atributo booleano para conocer si el boton cap fue presionado

            self.__ui.btn30.setText("ABC")
            self.__ui.btn21.setText("=\\<")

            self.__ui.btn1.setText('1')
            self.__ui.btn2.setText('2')
            self.__ui.btn3.setText('3')
            self.__ui.btn4.setText('4')
            self.__ui.btn5.setText('5')
            self.__ui.btn6.setText('6')
            self.__ui.btn7.setText('7')
            self.__ui.btn8.setText('8')
            self.__ui.btn9.setText('9')
            self.__ui.btn10.setText('0')
            self.__ui.btn11.setText('@')
            self.__ui.btn12.setText('#')
            self.__ui.btn13.setText('$')
            self.__ui.btn14.setText('_')
            self.__ui.btn15.setText('&')
            self.__ui.btn16.setText('-')
            self.__ui.btn17.setText('+')
            self.__ui.btn18.setText('(')
            self.__ui.btn19.setText(')')
            self.__ui.btn20.setText('/')

            self.__ui.btn22.setText('*')
            self.__ui.btn23.setText('"')
            self.__ui.btn24.setText("'")
            self.__ui.btn25.setText(':')
            self.__ui.btn26.setText(';')
            self.__ui.btn27.setText('!')
            self.__ui.btn28.setText('?')

        
        else:
            self.__numbersCharsStatus = False #Cambia el estado del boton a no presionado
            self.__numberCharsStatus_2 = False #Cambia el estado del boton de caracteres extra a no presionado
            self.__ui.btn30.setText("?123")
            self.__ui.btn21.setText("Mayús")
            #Devuelve las letras dependiendo el estad que tuviera el boton capitalizar
            if not self.__capStatus:
                self.__set_minus()
            else:
                self.__set_mayus() 
        self.__focusLine.setFocus()   

    def __set_mayus(self):
        self.__ui.btn1.setText('Q')
        self.__ui.btn2.setText('W')
        self.__ui.btn3.setText('E')
        self.__ui.btn4.setText('R')
        self.__ui.btn5.setText('T')
        self.__ui.btn6.setText('Y')
        self.__ui.btn7.setText('U')
        self.__ui.btn8.setText('I')
        self.__ui.btn9.setText('O')
        self.__ui.btn10.setText('P')
        self.__ui.btn11.setText('A')
        self.__ui.btn12.setText('S')
        self.__ui.btn13.setText('D')
        self.__ui.btn14.setText('F')
        self.__ui.btn15.setText('G')
        self.__ui.btn16.setText('H')
        self.__ui.btn17.setText('J')
        self.__ui.btn18.setText('K')
        self.__ui.btn19.setText('L')
        self.__ui.btn20.setText('Ñ')

        self.__ui.btn22.setText('Z')
        self.__ui.btn23.setText('X')
        self.__ui.btn24.setText('C')
        self.__ui.btn25.setText('V')
        self.__ui.btn26.setText('B')
        self.__ui.btn27.setText('N')
        self.__ui.btn28.setText('M')

    def __set_minus(self):
        self.__ui.btn1.setText('q')
        self.__ui.btn2.setText('w')
        self.__ui.btn3.setText('e')
        self.__ui.btn4.setText('r')
        self.__ui.btn5.setText('t')
        self.__ui.btn6.setText('y')
        self.__ui.btn7.setText('u')
        self.__ui.btn8.setText('i')
        self.__ui.btn9.setText('o')
        self.__ui.btn10.setText('p')
        self.__ui.btn11.setText('a')
        self.__ui.btn12.setText('s')
        self.__ui.btn13.setText('d')
        self.__ui.btn14.setText('f')
        self.__ui.btn15.setText('g')
        self.__ui.btn16.setText('h')
        self.__ui.btn17.setText('j')
        self.__ui.btn18.setText('k')
        self.__ui.btn19.setText('l')
        self.__ui.btn20.setText('ñ')

        self.__ui.btn22.setText('z')
        self.__ui.btn23.setText('x')
        self.__ui.btn24.setText('c')
        self.__ui.btn25.setText('v')
        self.__ui.btn26.setText('b')
        self.__ui.btn27.setText('n')
        self.__ui.btn28.setText('m')


class NumericKeyboardWidget(QWidget):
    def __init__(self, focusLine, natural_numbers:bool = False):
        QWidget.__init__(self)
        self.__ui = Numeric_Keyboard()
        self.__ui.setupUi(self)
        self.__focusLine = focusLine 
        self.__focusLine.setFocus() 
        self.__natural_numbers:bool = natural_numbers
        self.__init_ui_components()

        self.__timerBackSpace = QTimer(self)
        self.__timerBackSpace.setInterval(1000)
        self.__timerBackSpace.setSingleShot(True)
        self.__timerBackSpace.timeout.connect(self.__backspaceHeld)

        # Lista de botones
        buttons = [
            self.__ui.btn1, self.__ui.btn2, self.__ui.btn3, self.__ui.btn4, self.__ui.btn5, 
            self.__ui.btn6, self.__ui.btn7, self.__ui.btn8, self.__ui.btn9, self.__ui.btn10,
            self.__ui.btn11, self.__ui.btn12
        ]

        # Conectar todos los botones al evento clicked
        for button in buttons:
            button.clicked.connect(self.__btnClicked)


        self.__ui.btn13.pressed.connect(self.__backspacePressed)  # Backspace
        self.__ui.btn13.released.connect(self.__backspaceReleased)  # Backspace

    def __init_ui_components(self):
        if self.__natural_numbers:
            self.__ui.btn11.hide()
            self.__ui.btn12.hide()

    def changeFocusKeyboard(self, focus):
        self.__focusLine = focus
        self.__focusLine.setFocus()

    def __btnClicked(self):
        button = self.sender()
        buttonText = button.text()
        self.__focusLine.setText(self.__focusLine.text() + buttonText)
        self.__focusLine.setFocus()


    def __backspacePressed(self):
        self.__timerBackSpace.start()
        button = self.sender()
        self.__focusLine.setText(self.__focusLine.text()[:-1])

    def __backspaceReleased(self):
        self.__timerBackSpace.stop()
        button = self.sender()
        self.__focusLine.setFocus()   

    def __backspaceHeld(self):
        self.__focusLine.clear()
        self.__focusLine.setFocus()