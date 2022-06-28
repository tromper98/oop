from interfaces.person.iperson import IPerson
from interfaces.base.ibasevehicle import IBaseVehicle


class IBus(IBaseVehicle):
    def add_passenger(self, passenger: IPerson) -> None:
        ...
