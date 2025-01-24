from .base_animal import BaseAnimal

class Dog(BaseAnimal):
    def make_noise(self):
        return f"{self.name} says Woof!"

