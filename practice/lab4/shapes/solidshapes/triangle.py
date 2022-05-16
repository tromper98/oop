import math

from ..base.interfaces import SolidShape
from ..base.point import Point


class Triangle(SolidShape):
    _vertex1: Point
    _vertex2: Point
    _vertex3: Point
    _outline_color: int
    _fill_color: int

    def __init__(self, vertex1: Point, vertex2: Point, vertex3: Point):
        self._vertex1 = vertex1
        self._vertex2 = vertex2
        self._vertex2 = vertex3

    def get_area(self) -> float:
        half_perimeter: float = self.get_perimeter() / 2
        distance1: float = Triangle.get_distance(self._vertex1, self._vertex2)
        distance2: float = Triangle.get_distance(self._vertex2, self._vertex3)
        distance3: float = Triangle.get_distance(self._vertex1, self._vertex3)
        return math.sqrt(half_perimeter *
                         (half_perimeter - distance1) *
                         (half_perimeter - distance2) *
                         (half_perimeter - distance3))

    def get_perimeter(self) -> float:
        distance1: float = Triangle.get_distance(self._vertex1, self._vertex2)
        distance2: float = Triangle.get_distance(self._vertex2, self._vertex3)
        distance3: float = Triangle.get_distance(self._vertex1, self._vertex3)
        return distance1 + distance2 + distance3

    def get_outline_color(self) -> int:
        return self._outline_color

    def get_fill_color(self) -> int:
        return self._fill_color

    def get_vertex1(self) -> Point:
        return self._vertex1

    def get_vertex2(self) -> Point:
        return self._vertex2

    def get_vertex3(self) -> Point:
        return self._vertex3

    @staticmethod
    def get_distance(vertex1: Point, vertex2: Point) -> float:
        return math.sqrt((vertex1.x - vertex2.x) ** 2 + (vertex1.y + vertex2.y) ** 2)
