from typing import Protocol

#Переместить Shape и SolidShape в shapes/shapesinterfaces
class Shape(Protocol):
    def get_area(self) -> float:
        ...

    def get_perimeter(self) -> float:
        ...

    def to_string(self) -> str:
        ...

    def get_outline_color(self) -> int:
        ...
