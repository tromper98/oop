from typing import List
import math

from point import Point
from .triangleimpl import TriangleImpl
from canvas.canvasinterfaces import CanvasDrawable, ICanvas


class Triangle(TriangleImpl, CanvasDrawable):
    def __init__(self,
                 vertex1: Point,
                 vertex2: Point,
                 vertex3: Point,
                 outline_color: int,
                 fill_color: int):
        super().__init__(vertex1, vertex2, vertex3, outline_color, fill_color)

    def get_area(self) -> float:
        half_perimeter: float = self.get_perimeter() / 2
        distance1: float = self._vertex1.distance_to_point(self._vertex2)
        distance2: float = self._vertex2.distance_to_point(self._vertex3)
        distance3: float = self._vertex1.distance_to_point(self._vertex3)
        return math.sqrt(half_perimeter *
                         (half_perimeter - distance1) *
                         (half_perimeter - distance2) *
                         (half_perimeter - distance3))

    def get_perimeter(self) -> float:
        distance1: float = self._vertex1.distance_to_point(self._vertex2)
        distance2: float = self._vertex2.distance_to_point(self._vertex3)
        distance3: float = self._vertex1.distance_to_point(self._vertex3)
        return distance1 + distance2 + distance3

    def get_outline_color(self) -> int:
        return self._outline_color

    def get_fill_color(self) -> int:
        return self._fill_color

    def to_string(self) -> str:
        report = f"""
        Triangle
        Vertex1: {self.get_vertex1().to_string}
        Vertex2: {self.get_vertex2().to_string}
        Vertex3: {self.get_vertex3().to_string}
        Perimeter: {round(self.get_perimeter(), 4)}
        Area: {round(self.get_area(), 4)}
        """
        return report

    def get_vertex1(self) -> Point:
        return self._vertex1

    def get_vertex2(self) -> Point:
        return self._vertex2

    def get_vertex3(self) -> Point:
        return self._vertex3

    def draw(self, canvas: ICanvas):
        points: List[Point] = [self.get_vertex1(), self.get_vertex2(), self.get_vertex3()]

        canvas.draw_line(self.get_vertex1(), self.get_vertex2(), self.get_outline_color())
        canvas.draw_line(self.get_vertex2(), self.get_vertex3(), self.get_outline_color())
        canvas.draw_line(self.get_vertex3(), self.get_vertex1(), self.get_outline_color())

        canvas.fill_polygon(points, self.get_fill_color())