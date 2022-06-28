from interfaces.car.iracingcar import IRacingCar
from interfaces.person.iracer import IRacer
from vehicleimpl import VehicleImpl


class RacingCar(IRacingCar, VehicleImpl):
    def add_passenger(self, passenger: IRacer) -> None:
        super().add_passenger(passenger)
