from .base_animal import BaseAnimal

class Cow(BaseAnimal):
    def make_noise(self):
        return f"{self.name} says Moo!"

