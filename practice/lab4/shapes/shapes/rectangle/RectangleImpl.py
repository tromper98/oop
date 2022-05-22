from shapes.base import BaseShape
from point import Point
from exceptions import InvalidRectangle


class RectangleImpl(BaseShape):
    _left_top: Point
    _right_bottom: Point
    _outline_color: int
    _fill_color: int

    def __init__(self, left_top: Point, right_bottom: Point, outline_color: int, fill_color: int):
        super().__init__(outline_color, fill_color)
        if not RectangleImpl.is_valid_rectangle(left_top, right_bottom):
            raise InvalidRectangle

        self._left_top = left_top
        self._right_bottom = right_bottom
        self._outline_color = outline_color
        self._fill_color = fill_color

    @staticmethod
    def is_valid_rectangle(left_top: Point, right_bottom: Point) -> bool:
        if left_top == right_bottom:
            return False
        return True
