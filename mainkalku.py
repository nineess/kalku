import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from kalkuu import Ui_MainWindow


class Calculator(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.current_input = ""

        self.btn0.clicked.connect(lambda: self.add_input('0'))
        self.btn1.clicked.connect(lambda: self.add_input('1'))
        self.btn2.clicked.connect(lambda: self.add_input('2'))
        self.btn3.clicked.connect(lambda: self.add_input('3'))
        self.btn4_2.clicked.connect(lambda: self.add_input('4'))
        self.btn5.clicked.connect(lambda: self.add_input('5'))
        self.btn6.clicked.connect(lambda: self.add_input('6'))
        self.btn7.clicked.connect(lambda: self.add_input('7'))
        self.btn8.clicked.connect(lambda: self.add_input('8'))
        self.btn9.clicked.connect(lambda: self.add_input('9'))

        self.btnplus.clicked.connect(self.plus)
        self.btnminus.clicked.connect(self.minus)
        self.btnmultiply.clicked.connect(self.multiply)
        self.btndivide.clicked.connect(self.divide)
        self.btnequal.clicked.connect(self.calculate)

        self.btnclear.clicked.connect(self.clear_input)

        self.pbtconvert.clicked.connect(self.convert_currency)

        self.actionquit.triggered.connect(self.close)

        self.result = "0"
        self.operator = ""
        self.first_operand = ""

        self.currency_rates = {
            'GEL': {'GEL': 1.0, 'USD': 0.37, 'EUR': 0.34},
            'USD': {'GEL': 2.70, 'USD': 1.0, 'EUR': 0.92},
            'EUR': {'GEL': 2.94, 'USD': 1.09, 'EUR': 1.0}
        }

    def add_input(self, value):
        self.current_input += value
        self.txtresult.setText(self.current_input)

    def clear_input(self):
        self.current_input = ""
        self.txtresult.clear()
        self.result = "0"
        self.operator = ""
        self.first_operand = ""

    def plus(self):
        self.operator = "+"
        self.result = self.txtresult.text()
        self.first_operand = self.result
        self.current_input = ""

    def minus(self):
        self.operator = "-"
        self.result = self.txtresult.text()
        self.first_operand = self.result
        self.current_input = ""

    def divide(self):
        self.operator = "/"
        self.result = self.txtresult.text()
        self.first_operand = self.result
        self.current_input = ""

    def multiply(self):
        self.operator = "*"
        self.result = self.txtresult.text()
        self.first_operand = self.result
        self.current_input = ""

    def calculate(self):
        if not (self.result == "0" or self.operator == ""):
            try:
                a = float(self.result)
                b = float(self.txtresult.text())
                second_operand = self.txtresult.text()
            except ValueError:
                QMessageBox.warning(self, "Error", "Invalid number")
                self.clear_input()
                return

            try:
                if self.operator == "+":
                    result = a + b
                elif self.operator == "-":
                    result = a - b
                elif self.operator == "/":
                    if b == 0:
                        QMessageBox.warning(self, "Error", "Cannot divide by zero")
                        self.clear_input()
                        return
                    result = a / b
                elif self.operator == "*":
                    result = a * b
                else:
                    QMessageBox.warning(self, "Error", "Unknown operator")
                    self.clear_input()
                    return

                if result == int(result):
                    result_str = str(int(result))
                else:
                    result_str = str(result)

                equation = f"{self.first_operand} {self.operator} {second_operand} = {result_str}"
                self.txtresult.setText(equation)

                self.current_input = result_str

                self.operator = ""
                self.result = "0"
                self.first_operand = ""

            except Exception as e:
                QMessageBox.warning(self, "Error", f"Calculation error: {str(e)}")
                self.clear_input()

    def convert_currency(self):
        try:
            amount = float(self.txtresult.text())
            from_currency = self.comboBoxFROM.currentText()
            to_currency = self.comboBoxTO.currentText()
            rate = self.currency_rates[from_currency][to_currency]
            converted_amount = amount * rate
            self.txtresult.setText(f"{converted_amount:.2f}")
            self.current_input = str(converted_amount)
        except ValueError:
            QMessageBox.warning(self, "Error", "Please enter a valid number first")





app = QApplication(sys.argv)
calculator = Calculator()
calculator.show()
sys.exit(app.exec())
