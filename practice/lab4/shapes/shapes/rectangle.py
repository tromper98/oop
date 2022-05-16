from typing import Optional

from base.interfaces import SolidShape
from base.point import Point
from base.exceptions import InvalidRectangle, InvalidOutlineColor, InvalidFillColor


class Rectangle(SolidShape):
    _left_top: Point
    _right_bottom: Point
    _outline_color: Optional[int]
    _fill_color: Optional[int]

    def __init__(self, left_top: Point, right_bottom: Point, outline_color: Optional[int], fill_color: Optional[int]):
        if not Rectangle.is_valid_rectangle(left_top, right_bottom):
            raise InvalidRectangle
        if not Rectangle.is_valid_color_number(outline_color):
            raise InvalidOutlineColor
        if not Rectangle.is_valid_color_number(fill_color):
            raise InvalidFillColor

        self._left_top = left_top
        self._right_bottom = right_bottom
        self._outline_color = outline_color
        self._fill_color = fill_color

    def get_height(self) -> float:
        return abs(self._left_top.y - self._right_bottom.y)

    def get_width(self) -> float:
        return abs(self._left_top.x - self._right_bottom.x)

    def get_area(self) -> float:
        height: float = self.get_height()
        width: float = self.get_width()
        return height * width

    def to_string(self) -> str:
        report = f"""
        Rectangle:
        Left top: {self.get_left_top().to_string}
        Right top: {self.get_right_bottom().to_string}
        Perimeter: {self.get_perimeter()}
        Area: {self.get_area()}
        """
        return report

    def get_outline_color(self) -> int:
        return self._outline_color

    def get_fill_color(self) -> int:
        return self._fill_color

    def get_left_top(self) -> Point:
        return self._left_top

    def get_right_bottom(self) -> Point:
        return self._right_bottom

    @staticmethod
    def is_valid_rectangle(left_top: Point, right_bottom: Point) -> bool:
        if left_top == right_bottom:
            return False
        return True

    @staticmethod
    def is_valid_color_number(number: int) -> bool:
        if number % 10 != 0:
            return False
        if 0 <= number <= 2**32:
            return True
        return False