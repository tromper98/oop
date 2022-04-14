from practice.lab3.car.gearbox.Gear import *


class Car:
    speed: int
    gear: Gear
    engine: bool

    def __init__(self):
        self.speed = 0
        self.gear = NeutralGear()
        self.engine = False

    def engine_on(self):
        if self.engine:
            return True

    def engine_off(self):
        if not self.engine:
            return True

        if self.engine and self.gear == NeutralGear and self.speed == 0:
            self.engine = False
            return True

        return False
