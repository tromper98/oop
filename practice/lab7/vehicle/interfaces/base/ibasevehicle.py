from typing import Protocol

from ipassenger import IPassenger


class IBaseVehicle(Protocol):
    def get_place_count(self) -> int:
        ...

    def get_passenger_count(self) -> int:
        ...

    def remove_all_passengers(self) -> None:
        ...
    
    def is_full(self) -> bool:
        ...

    def is_empty(self) -> bool:
        ...

    def get_passenger(self, index: int) -> IPassenger:
        ...

    def add_passenger(self, passenger: IPassenger) -> None:
        ...

    def remove_passenger(self, index: int) -> None:
        ...
