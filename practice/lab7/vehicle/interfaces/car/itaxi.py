from interfaces.person.iperson import IPerson
from icar import ICar


class ITaxi(ICar):
    def add_passenger(self, passenger: IPerson) -> None:
        ...
