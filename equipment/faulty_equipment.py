from .equipment import Equipment

class FaultyEquipment(Equipment):
    def operate(self):
        raise RuntimeError(f"{self.name} has malfunctioned!")
    
    def fix(self):
        self.__class__ = Equipment

