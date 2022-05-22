from typing import Protocol

from base.exceptions import InvalidOutlineColor


# Переместить Shape и SolidShape в shapes/shapesinterfaces
class Shape(Protocol):
    def get_area(self) -> float:
        ...

    def get_perimeter(self) -> float:
        ...

    def to_string(self) -> str:
        ...

    def get_outline_color(self) -> int:
        ...

    @staticmethod
    def is_valid_color_number(number: int) -> bool:
        if 0 <= number <= 2 ** 32:
            return True
        return False
