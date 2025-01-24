from .crop import Crop

class Rice(Crop):
    def __init__(self):
        self._setName(Rice.getName)

    def getName():
        return 'rice'

    def water_req(self):
        return "4 litres"

