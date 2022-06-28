from interfaces.person.iracer import IRacer
from icar import ICar


class IRacingCar(ICar):
    def add_passenger(self, passenger: IRacer) -> None:
        ...
