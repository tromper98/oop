from shapes.shapeinterfaces import SolidShape
from base.exceptions import InvalidCircle, InvalidOutlineColor, InvalidFillColor
from point import Point


class CircleImpl(SolidShape):
    _center: Point
    _radius: float
    _outline_color: int
    _fill_color: int

    def __init__(self, center: Point, radius: float, outline_color: int, fill_color: int):
        if not CircleImpl.is_valid_radius(radius):
            raise InvalidCircle()
        if not CircleImpl.is_valid_color_number(outline_color):
            raise InvalidOutlineColor(outline_color)
        if not CircleImpl.is_valid_color_number(fill_color):
            raise InvalidFillColor(outline_color)

        self._center = center
        self._radius = radius
        self._outline_color = outline_color
        self._fill_color = fill_color

    @staticmethod
    def is_valid_radius(radius: float) -> bool:
        return False if radius <= 0 else True
