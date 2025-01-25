from farm import Farm
from animals.dog import Dog
from animals.cow import Cow
from animals.chicken import Chicken
from animals.cat import Cat
from crops import *
from equipment.equipment import Equipment
from equipment.faulty_equipment import FaultyEquipment

if __name__ == "__main__":
    farm = Farm()

    # Add animals
    farm.add_animal(Dog("Buddy"))
    farm.add_animal(Cow("Bessie"))
    farm.add_animal(Chicken("Clucky"))
    farm.add_animal(Cat("Mawler"))

    # Add crops
    farm.add_crop(Corn())
    farm.add_crop(Wheat())
    farm.add_crop(Rice())
    farm.add_crop(Potato())

    # Add equipment
    farm.add_equipment(Equipment("Tractor"))
    farm.add_equipment(FaultyEquipment("Plow"))
    farm.add_equipment(Equipment("Old Harvester"))
    farm.add_equipment(Equipment("Bailer"))

    # Run the farm and print animal noises
    print(farm.run_farm())
    print()

    print("Crops being grown:")
    print(farm.grow_crops())
    print()

    print("Crops need:")
    print(farm.crop_needs())
    print()

    # Operate all equipment and handle exceptions
    print("Operating equipment:")
    print(farm.operate_all_equipment())

