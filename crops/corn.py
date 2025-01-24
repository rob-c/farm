from .crop import Crop

class Corn(Crop):
    def __init__(self):
        self._setName(Corn.getName)

    def getName():
        return 'corn'

    def water_req(self):
        return "2 litres"
