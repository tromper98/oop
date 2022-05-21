from __future__ import annotations
import math


class Point:
    _x: float
    _y: float

    def __init__(self, x: float, y: float):
        self._x = x
        self._y = y

    @property
    def x(self) -> float:
        return self._x

    @property
    def y(self) -> float:
        return self._y

    @property
    def to_string(self) -> str:
        return f'({self._x}, {self._y})'

    def distance_to_point(self, point: Point):
        math.sqrt(
            (self.x - point.x) ** 2 +
            (self.y + point.y) ** 2)

    def __eq__(self, other) -> bool:
        if self.x == other.x and self.y == other.y:
            return True
        return False
