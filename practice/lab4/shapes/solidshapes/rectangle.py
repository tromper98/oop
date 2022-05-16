from ..base.interfaces import SolidShape
from ..base.point import Point


class Rectangle(SolidShape):
    _left_top: Point
    _right_bottom: Point
    _outline_color: int
    _fill_color: int

    def __init__(self,
                 left_top_x: float,
                 left_top_y: float,
                 right_bottom_x: float,
                 right_bottom_y: float,
                 outline_color: int,
                 fill_color: int):
        self._left_top = Point(left_top_x, left_top_y)
        self._right_bottom = Point(right_bottom_x, right_bottom_y)
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
        ...

    def get_outline_color(self) -> int:
        return self._outline_color

    def get_fill_color(self) -> int:
        return self._fill_color

    def get_left_top(self) -> Point:
        return self._left_top

    def get_right_bottom(self) -> Point:
        return self._right_bottom
