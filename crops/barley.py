from .crop import Crop

class Barley(Crop):
    def __init__(self):
        self._setName(Barley.getName)

    def getName():
        return 'barley'
    
    def water_req(self):
        return '2 litres'