import math

from base.interfaces import SolidShape
from base.point import Point
from base.exceptions import InvalidCircle, InvalidOutlineColor, InvalidFillColor


class Circle(SolidShape):
    _center: Point
    _radius: float
    _outline_color: int
    _fill_color: int

    def __init__(self, center: Point, radius: float, outline_color: int, fill_color: int):
        if not Circle.is_valid_circle(radius):
            raise InvalidCircle()
        if not Circle.is_valid_color_number(outline_color):
            raise InvalidOutlineColor(outline_color)
        if not Circle.is_valid_color_number(fill_color):
            raise InvalidFillColor(outline_color)

        self._center = center
        self._radius = radius
        self._outline_color = outline_color
        self._fill_color = fill_color

    def get_area(self) -> float:
        return math.pi * self._radius ** 2

    def get_perimeter(self) -> float:
        return 2 * math.pi * self._radius

    def to_string(self) -> str:
        report: str = f"""
        Circle
        Center: {self.get_center().to_string}
        Radius: {self.get_radius()}
        Perimeter: {round(self.get_perimeter(), 4)}
        Area: {round(self.get_area(), 4)}
        """
        return report

    def get_outline_color(self) -> int:
        return self._outline_color

    def get_fill_color(self) -> int:
        return self._fill_color

    def get_center(self) -> Point:
        return self._center

    def get_radius(self) -> float:
        return self._radius

    @staticmethod
    def is_valid_circle(radius: float) -> bool:
        return False if radius <= 0 else True

    @staticmethod
    def is_valid_color_number(number: int) -> bool:
        if 0 <= number <= 2**32:
            return True
        return False
