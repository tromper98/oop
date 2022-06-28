from interfaces.base.ibasevehicle import IBaseVehicle
from interfaces.base.ipassenger import IPassenger


from typing import List


class VehicleImpl(IBaseVehicle):
    _make_of_car: str
    _place_count: int
    _passengers: List[IPassenger]

    def __init__(self, make_of_car: str, place_count:int):
        self._make_of_car = make_of_car
        self._place_count = place_count

    def get_passenger_count(self) -> int:
        return self._place_count

    def remove_all_passengers(self) -> None:
        self._passengers.clear()

    def is_full(self) -> bool:
        return len(self._passengers) == self._place_count

    def is_empty(self) -> bool:
        return True if len(self._passengers) == 0 else False

    def get_passenger(self, index: int) -> IPassenger:
        return self._passengers[index]

    def add_passenger(self, passenger) -> None:
        self._passengers.append(passenger)

    def remove_passenger(self, index: int) -> None:
        del self._passengers[index]
