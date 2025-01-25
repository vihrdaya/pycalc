import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui


class PadButton(QtWidgets.QWidget):
    def __init__(self, value):
        super().__init__()

        self.button = QtWidgets.QPushButton(f"{value}")


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.hello = ["Hello"]
        self.num_1 = "1"
        self.pad_button_1 = PadButton(f"{self.num_1}")
        self.text = QtWidgets.QLabel("This is a Label", alignment=QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.addButton(self.pad_button_1)
        # self.layout.addWidget(self.pad_button_1.button)

    @QtCore.Slot()
    def addButton(self, pad_button):
        self.layout.addWidget(pad_button.button)
        pad_button.button.clicked.connect(self.magic)

    @QtCore.Slot()
    def magic(self):
        self.text.setText(random.choice(self.num_1))


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())
