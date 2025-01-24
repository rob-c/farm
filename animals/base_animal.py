
class BaseAnimal:
    def __init__(self, name):
        self.name = name

    def make_noise(self):
        raise NotImplementedError("Subclasses must implement make_noise method")

