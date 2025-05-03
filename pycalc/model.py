class CalculatorModel:
    def __init__(self):
        self.operate = []

    def input(self, value):
        if value == "=":
            return self.evaluate()
        elif value == "CE":
            self.operate = []
            return ""

    def evaluate(self):
        try:
            result = eval("".join(self.operate))
            self.operate = [str(result)]
            return str(result)
        except Exception:
            return "Error"
