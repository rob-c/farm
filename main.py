from farm import Farm
from animals.dog import Dog
from animals.cow import Cow
from animals.chicken import Chicken
from animals.goose import Goose
from crops import *
from equipment.equipment import Equipment
from equipment.faulty_equipment import FaultyEquipment
from equipment.rusty_equipment import RustyEquipment

if __name__ == "__main__":
    farm = Farm()

    # Add animals
    farm.add_animal(Dog("Buddy"))
    farm.add_animal(Cow("Bessie"))
    farm.add_animal(Chicken("Clucky"))
    farm.add_animal(Goose("Silly"))

    # Add crops
    farm.add_crop(Corn())
    farm.add_crop(Wheat())
    farm.add_crop(Rice())
    farm.add_crop(Barley())

    # Add equipment
    farm.add_equipment(Equipment("Tractor"))
    farm.add_equipment(Equipment("Plow"))

    old_harv = FaultyEquipment("Old Harvester")
    farm.add_equipment(old_harv)

    farm.add_equipment(RustyEquipment("Sickle"))

    # Run the farm and print animal noises
    print()
    print("=========")
    print("FIRST RUN")
    print("=========")
    print()

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

    # Fix the Old Harvester

    old_harv.fix()

    print()
    print("==========")
    print("SECOND RUN")
    print("==========")
    print()

    print("Operating equipment:")
    print(farm.operate_all_equipment())




