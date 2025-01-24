from animals.dog import Dog
from animals.cow import Cow
from animals.chicken import Chicken
from crops import *
from equipment.equipment import Equipment
from cowsay import cowsay
from lolpython import lol_py

class Farm:
    def __init__(self):
        self.animals = []
        self.crops = []
        self.equipment = []

        lol_py(cowsay('Welcome to the Python Farm'))

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_crop(self, crop):
        self.crops.append(crop)

    def add_equipment(self, equipment):
        self.equipment.append(equipment)

    def operate_all_equipment(self):
        results = []
        for eq in self.equipment:
            try:
                results.append(eq.operate())
            except Exception as e:
                results.append(f"Error operating {eq.name}: {str(e)}")
        return "\n".join(results)

    def grow_crops(self):
        growing = [crop.grow() for crop in self.crops]
        return "\n".join(growing)

    def crop_needs(self):
        needs = [crop.water_needs() for crop in self.crops]
        return "\n".join(needs)

    def apply_to_crops(self, functor):
        results = [functor(crop) for crop in self.crops]
        return "\n".join(results)

    def run_farm(self):
        # Using functors
        water_functor = WaterCrop(10)
        fertilize_functor = FertilizeCrop("Nitrogen", 5)

        msg  = "Running Farm:\n"
        msg += "\n"
        msg += "Applying water to crops:\n"
        msg += self.apply_to_crops(water_functor)

        msg += "\n\n"
        msg += "Applying fertilizer to crops:\n"
        msg += self.apply_to_crops(fertilize_functor)

        msg += "\n\n"
        msg += "Animal noises:\n"
        msg += "\n".join([animal.make_noise() for animal in self.animals])

        msg += "\nGoodbye!"
        
        return msg

