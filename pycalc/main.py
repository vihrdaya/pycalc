import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui


class PadButton(QtWidgets.QWidget):
    def __init__(self, value):
        super().__init__()


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.hello = ["Hello"]
        self.operate = []
        # self.num_1 = "1"
        # self.pad_button_1 = PadButton(f"{self.num_1}")
        self.text = QtWidgets.QLabel(f'{" ".join(self.operate)}', alignment=QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.buttons = []
        # self.addButton(self.num_1)
        for i in range(10):
            str(i)
            self.addButton(str(i))
        operator_signs = ['+', '=']
        for i in operator_signs:
            self.addButton(i)
        self.addButton('CE')
    @QtCore.Slot()
    def addButton(self, value):
        pad_button = QtWidgets.QPushButton(f"{value}")
        self.layout.addWidget(pad_button)
        self.buttons.append(pad_button)
        pad_button.clicked.connect(lambda _, v=value: self.magic(v))

    @QtCore.Slot()
    def magic(self, value):
        self.operate.append(value)
        self.text.setText(f'{"".join(self.operate)}')

        if value == '=':

            self.operate = [str(self.math_do(self.operate))]
            self.text.setText(f'{"".join(self.operate)}')
        
        if value == 'CE':
            self.operate = []
            self.text.setText(f'{"".join(self.operate)}')
    
    def math_do(self, operands: list) -> float:
        for i in operands:
            if i == '+':
                ans = self.additionAction(operands)
                return ans
    
    def open_close_recursion(self, inside_nums: dict) -> None:
        open_close_counter = 0
        position_log = 0
        for i in inside_nums:
            if i == '(':
                open_close_counter += 1
                position_log 

    def parenthesis_pairer(self, operands: list) -> None:
        operation_pairs = {
            'pairs': [],
            'level': 0,
        }
        open_close_counter = 0
        position_log = 0
        print(operands)
        
    def num_parser(self, operands:list) -> None:
        self.parenthesis_pairer(operands)


    

    def additionAction(self, operands: list) -> float:
        operands.remove('+')
        operands.remove('=')
        operands = [int(i) for i in operands]
        return sum(operands)




if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())
