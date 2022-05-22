from base.exceptions import InvalidTriangle
from shapes.base import BaseShape
from point import Point


class TriangleImpl(BaseShape):
    _vertex1: Point
    _vertex2: Point
    _vertex3: Point
    _outline_color: int
    _fill_color: int

    def __init__(self,
                 vertex1: Point,
                 vertex2: Point,
                 vertex3: Point,
                 outline_color: int,
                 fill_color: int):
        super().__init__(outline_color, fill_color)
        if not TriangleImpl.is_valid_triangle(vertex1, vertex2, vertex3):
            raise InvalidTriangle()

        self._vertex1 = vertex1
        self._vertex2 = vertex2
        self._vertex3 = vertex3
        self._outline_color = outline_color
        self._fill_color = fill_color

    @staticmethod
    def is_valid_triangle(vertex1: Point, vertex2: Point, vertex3: Point) -> bool:

        if vertex1 == vertex2:
            return False

        if vertex1 == vertex3:
            return False

        if vertex2 == vertex3:
            return False

        return True
