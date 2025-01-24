
class Crop:
    def __init__(self):
        self.name = None

    def _setName(self, name):
        self.name = name

    def grow(self):
        return f"The {self.name()} crop is growing."

    def water_needs(self):
        return f"{self.name()} crop needs {self.water_req()} water."

