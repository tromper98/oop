from .gear import Gear


class NeutralGear(Gear):
    #Вместо класса можно обойтись константой
    def __init__(self, min_speed=None, max_speed=None):
        code = 0
        super().__init__(code, min_speed, max_speed)
