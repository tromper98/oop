import math

from ..base.interfaces import Shape
from ..base.point import Point


class LineSegment(Shape):
    _start_point: Point
    _end_point: Point
    _outline_color: int

    def __init__(self, start_point: Point, end_point: Point, outline_color: int):
        self._start_point = start_point
        self._end_point = end_point
        self._outline_color = outline_color

    def get_area(self) -> float:
        return 0

    def get_perimeter(self) -> float:
        return math.sqrt(
            (self._start_point.x - self._end_point.x) ** 2 +
            (self._start_point.y + self._end_point.y) ** 2)

    def to_string(self) -> str:
        ...

    def get_outline_color(self) -> int:
        return self._outline_color

    def get_start_point(self) -> Point:
        return self._start_point

    def get_end_point(self) -> Point:
        return self._end_point
