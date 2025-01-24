from .base_animal import BaseAnimal

class Goose(BaseAnimal):
    def make_noise(self):
        return f"{self.name} says Honk!"