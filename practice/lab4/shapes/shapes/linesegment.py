import math
from typing import Optional

from base.interfaces import Shape
from base.point import Point
from base.exceptions import InvalidOutlineColor


class LineSegment(Shape):
    _start_point: Point
    _end_point: Point
    _outline_color: Optional[int]

    def __init__(self, start_point: Point, end_point: Point, outline_color: Optional[int]):
        if not LineSegment.is_valid_color_number(outline_color):
            raise InvalidOutlineColor

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
        report: str = f"""
        Line Segment
        Start point: {self.get_start_point().to_string}
        End point: {self.get_end_point().to_string}
        Perimeter: {self.get_perimeter()}
        """
        return report

    def get_outline_color(self) -> int:
        return self._outline_color

    def get_start_point(self) -> Point:
        return self._start_point

    def get_end_point(self) -> Point:
        return self._end_point

    @staticmethod
    def is_valid_color_number(number: int) -> bool:
        if number % 10 != 0:
            return False
        if 0 <= number <= 2**32:
            return True
        return False
