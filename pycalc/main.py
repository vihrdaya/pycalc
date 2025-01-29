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
        # self.num_1 = "1"
        # self.pad_button_1 = PadButton(f"{self.num_1}")
        self.text = QtWidgets.QLabel("This is a Label", alignment=QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.buttons = []
        # self.addButton(self.num_1)
        for i in range(10):
            str(i)
            self.addButton(str(i))

    @QtCore.Slot()
    def addButton(self, value):
        pad_button = QtWidgets.QPushButton(f"{value}")
        self.layout.addWidget(pad_button)
        self.buttons.append(pad_button)
        pad_button.clicked.connect(lambda _, v=value: self.magic(v))

    @QtCore.Slot()
    def magic(self, value):
        self.text.setText(random.choice(value))


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())
