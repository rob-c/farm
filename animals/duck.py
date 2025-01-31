from .base_animal import BaseAnimal

class Duck(BaseAnimal):
    def make_noise(self):
        return f"{self.name} says Quack!"

