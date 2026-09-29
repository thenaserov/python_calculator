from PyQt5 import QtWidgets, uic
import sys
import os

os.system("cls")


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi("mainwindow.ui", self)

        self.text = ""

        self.pbNumberOne.clicked.connect(lambda: self.number_clicked("1"))
        self.pbNumberTwo.clicked.connect(lambda: self.number_clicked("2"))
        self.pbNumberThree.clicked.connect(lambda: self.number_clicked("3"))
        self.pbNumberFour.clicked.connect(lambda: self.number_clicked("4"))
        self.pbNumberFive.clicked.connect(lambda: self.number_clicked("5"))
        self.pbNumberSix.clicked.connect(lambda: self.number_clicked("6"))
        self.pbNumberSeven.clicked.connect(lambda: self.number_clicked("7"))
        self.pbNumberEight.clicked.connect(lambda: self.number_clicked("8"))
        self.pbNumberNine.clicked.connect(lambda: self.number_clicked("9"))
        self.pbNumberZero.clicked.connect(lambda: self.number_clicked("0"))

        self.pbDot.clicked.connect(self.dot_clicked)

        self.pbPlus.clicked.connect(lambda: self.operator_clicked("+"))
        self.pbNegative.clicked.connect(lambda: self.operator_clicked("-"))
        self.pbMultiply.clicked.connect(lambda: self.operator_clicked("*"))
        self.pbDevide.clicked.connect(lambda: self.operator_clicked("/"))

        self.pbEqual.clicked.connect(self.equal_clicked)
        self.pbDeleteAll.clicked.connect(self.clear_clicked)

        self.show()

    def number_clicked(self, number):
        self.text += number
        self.lineEdit.setText(self.text)

    def dot_clicked(self):
        current_number = self.text

        for operator in "+-*/":
            current_number = current_number.split(operator)[-1]

        if "." not in current_number:
            if not self.text or self.text[-1] in "+-*/":
                self.text += "0."
            else:
                self.text += "."

            self.lineEdit.setText(self.text)

    def operator_clicked(self, operator):
        if not self.text:
            return

        if self.text[-1] in "+-*/":
            self.text = self.text[:-1]

        self.text += operator
        self.lineEdit.setText(self.text)

    def equal_clicked(self):
        if not self.text:
            return

        if self.text[-1] in "+-*/":
            return

        try:
            result = eval(
                self.text,
                {"__builtins__": None},
                {}
            )

            if isinstance(result, float) and result.is_integer():
                result = int(result)

            self.text = str(result)
            self.lineEdit.setText(self.text)

        except ZeroDivisionError:
            self.text = ""
            self.lineEdit.setText("Cannot divide by zero")

        except Exception:
            self.text = ""
            self.lineEdit.setText("Error")

    def clear_clicked(self):
        self.text = ""
        self.lineEdit.clear()


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
sys.exit(app.exec_())
