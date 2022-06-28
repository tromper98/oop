from interfaces.person.ipoliceman import IPoliceMan
from icar import ICar


class IPoliceCar(ICar):
    def add_passenger(self, passenger: IPoliceMan) -> None:
        ...
