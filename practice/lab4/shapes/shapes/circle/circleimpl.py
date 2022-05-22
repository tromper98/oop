from shapes.base import BaseShape
from exceptions import InvalidCircle
from point import Point


class CircleImpl(BaseShape):
    _center: Point
    _radius: float
    _outline_color: int
    _fill_color: int

    def __init__(self, center: Point, radius: float, outline_color: int, fill_color: int):
        super().__init__(outline_color, fill_color)
        if not CircleImpl.is_valid_radius(radius):
            raise InvalidCircle()

        self._center = center
        self._radius = radius
        self._outline_color = outline_color
        self._fill_color = fill_color

    @staticmethod
    def is_valid_radius(radius: float) -> bool:
        return False if radius <= 0 else True
