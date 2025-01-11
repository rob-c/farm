from .crop import Crop

class Wheat(Crop):
    def __init__(self):
        self._setName(Wheat.getName)

    def getName():
        return 'wheat'

    def water_req(self):
        return "3 litres"
