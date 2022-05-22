import math

from point import Point
from .circleimpl import CircleImpl


class Circle(CircleImpl):
    def __init__(self, center: Point, radius: float, outline_color: int, fill_color: int):
        super().__init__(center, radius, outline_color, fill_color)

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

