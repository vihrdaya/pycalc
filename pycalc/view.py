from PySide6 import QtWidgets, QtCore


class CalculatorView(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QtWidgets.QVBoxLayout(self)

        self.text = QtWidgets.QLabel("", alignment=QtCore.Qt.AlignCenter)
        self.layout.addWidget(self.text)

        self.buttons = {}
        for label in list(map(str, range(10))) + ["+", "=", "CE"]:
            btn = QtWidgets.QPushButton(label)
            self.layout.addWidget(btn)
            self.buttons[label] = btn
