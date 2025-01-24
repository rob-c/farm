from .equipment import Equipment

class RustyEquipment(Equipment):
    def operate(self):
        return f"The {self.name} is operating, but it makes an awful noise."