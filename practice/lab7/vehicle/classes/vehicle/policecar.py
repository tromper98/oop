from interfaces.car.ipolicecar import IPoliceCar
from interfaces.person.ipoliceman import IPoliceMan
from vehicleimpl import VehicleImpl


class PoliceCar(IPoliceCar, VehicleImpl):
    def add_passenger(self, passenger: IPoliceMan) -> None:
        super().add_passenger(passenger)
