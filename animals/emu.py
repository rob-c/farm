from .base_animal import BaseAnimal

class Emu(BaseAnimal):
    def make_noise(self):
        return f"{self.name} says Cueftee!"