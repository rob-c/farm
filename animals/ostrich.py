from .base_animal import BaseAnimal

class Ostrich(BaseAnimal):
    def make_noise(self):
        return f"{self.name} says Honk!"

