from .base_animal import BaseAnimal

class Chicken(BaseAnimal):
    def make_noise(self):
        return f"{self.name} says Cluck!"

