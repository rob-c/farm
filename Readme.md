
# Farm Package Example

This repository serves as a small demonstration of how to work with classes, inheritance, and the importing of Python3 libraries in a modular structure. It features a `Farm` package that integrates animals, crops, and equipment, showcasing the following concepts:

- Class inheritance
- Passing functions as methods (functors)
- Handling exceptions
- Modular code organization

This project is designed to run requiring libraries not normally in a Python3 install and as such encourages you to use virtualenvs.

## Setting up via venv

Python3 has natively supported virtualenvs via the venv module for some time now. This is the recommended way to get running with Python3 Virtual Environments.

1. Setup a new env within this project:
```
> python3 -m venv env
```

You can technically use whatever foldername you prefer, but this project has an appropriate .gitignore rule for the `env\` folder which is a good indicator of what is within that folder.

2. Activate the new virtual env:
```
> source ./env/bin/activate
(env) > _
```

 (or Windows) 
```
.\env\Scripts\activate
```

3. Install this project into the new virtual env:
```
(env) > python3 -m pip install -r requirements.txt
```

4. Run the project
```
(env) > python3 main.py

...
```

5. Leave the virtualenv after you're finished:
```
(env) > deactivate
> _
```


## Directory Structure

```
.
├── animals
│   ├── base_animal.py
│   ├── chicken.py
│   ├── cow.py
│   ├── dog.py
│   └── __init__.py
├── crops
│   ├── corn.py
│   ├── crop.py
│   ├── crop_tasks.py
│   ├── __init__.py
│   ├── rice.py
│   └── wheat.py
├── equipment
│   ├── equipment.py
│   ├── faulty_equipment.py
│   └── __init__.py
├── farm.py
├── __init__.py
├── main.py
├── Readme.md
└── requirements.txt
```

## Key Components

### Animals

- `Dog`, `Cow`, and `Chicken` classes inherit from a `BaseAnimal` class and implement the `make_noise` method to produce unique sounds.

### Crops

- The `Crop` base class is extended by specific crop types such as `Corn`, `Wheat`, and `Rice`.
- Functors are used to simulate actions like watering and fertilizing crops.
- Functors are also used to track the crop name in this class(!).

### Equipment

- Equipment includes `Equipment` and `FaultyEquipment` classes, with methods to simulate operation.
- Faulty equipment raises exceptions to demonstrate error handling.

## Features

1. **Animal Management**
   - Add animals to the farm and retrieve their noises using the `runFarm` method.

2. **Crop Management**
   - Add crops to the farm and apply functors (e.g., watering or fertilizing) to simulate crop maintenance.

3. **Equipment Operation**
   - Operate all equipment on the farm, handling exceptions for faulty equipment.

4. **Passing Functions as Methods**
   - Use standalone functions (e.g., `harvest` and `inspect`) as dynamic methods for crops.

## Usage

1. Clone the repository:
   ```bash
   git clone <repo_url>
   cd project_root
   ```

2. Run the main script:
   ```bash
   python3 main.py
   ```

3. Observe the output:
   - Animal noises
   - Equipment operation results
   - Functor applications (e.g., watering and fertilizing crops)
   - Dynamic crop methods (e.g., harvesting and inspecting)

## Example Output

```
 ____________________________
< Welcome to the Python Farm >
 ----------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
Running Farm:

Applying water to crops:
corn received 10 liters of water.
wheat received 10 liters of water.
rice received 10 liters of water.

Applying fertilizer to crops:
corn was fertilized with 5 kg of Nitrogen.
wheat was fertilized with 5 kg of Nitrogen.
rice was fertilized with 5 kg of Nitrogen.

Animal noises:
Buddy says Woof!
Bessie says Moo!
Clucky says Cluck!

Crops being grown:
The corn crop is growing.
The wheat crop is growing.
The rice crop is growing.

Crops need:
corn crop needs 2 litres water.
wheat crop needs 3 litres water.
rice crop needs 4 litres water.

Operating equipment:
The Tractor is operating.
The Plow is operating.
Error operating Old Harvester: Old Harvester has malfunctioned!
```

## Learning Objectives

This repository is ideal for beginners learning about:
- Class-based object-oriented programming in Python
- Modular code organization
- Using functors and passing functions dynamically
- Handling exceptions gracefully in Python

Feel free to experiment by adding new animals, crops, or equipment and extending the functionality!


