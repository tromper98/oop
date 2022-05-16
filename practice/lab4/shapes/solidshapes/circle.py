import math

from ..base.interfaces import SolidShape
from ..base.point import Point


class Circle(SolidShape):
    _center: Point
    _radius: float
    _outline_color: int
    _fill_color: int

    def __init__(self, center: Point, radius: float, outline_color: int, fill_color: int):
        self._center = center
        self._radius = radius
        self._outline_color = outline_color
        self._fill_color = fill_color

    def get_area(self) -> float:
        return math.pi * self._radius ** 2

    def get_perimeter(self) -> float:
        return 2 * math.pi * self._radius

    def to_string(self) -> str:
        ...

    def get_outline_color(self) -> int:
        return self._outline_color

    def get_fill_color(self) -> int:
        return self._fill_color

    def get_center(self) -> Point:
        return self._center

    def get_radius(self) -> float:
        return self._radius
