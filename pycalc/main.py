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

        self.pad_button = PadButton("1")
        self.text = QtWidgets.QLabel("This is a Label", alignment=QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.pad_button.button)

        self.pad_button.button.clicked.connect(self.magic)

    @QtCore.Slot()
    def magic(self):
        self.text.setText(random.choice(self.hello))


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())
