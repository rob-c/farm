from .crop import Crop

class Potato(Crop):
    def __init__(self):
        self._setName(Potato.getName)

    def getName():
        return 'potato'

    def water_req(self):
        return "10 litres"
