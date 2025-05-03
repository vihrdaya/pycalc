class CalculatorController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        for label, button in self.view.buttons.items():
            button.clicked.connect(lambda _, v=label: self.handle_input(v))

    def handle_input(self, value):
        result = self.model.input(value)
        self.view.text.setText(result)
