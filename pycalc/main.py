import sys
from PySide6.QtWidgets import QApplication
from model import CalculatorModel
from view import CalculatorView
from controller import CalculatorController

if __name__ == "__main__":
    app = QApplication([])

    model = CalculatorModel()
    view = CalculatorView()
    controller = CalculatorController(model, view)

    view.resize(300, 400)
    view.show()

    sys.exit(app.exec())
