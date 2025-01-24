from .equipment import Equipment

class FaultyEquipment(Equipment):
    def operate(self):
        raise RuntimeError(f"{self.name} has malfunctioned!")

