from typing import List, Tuple

from canvas.canvasinterfaces import ICanvas
from point import Point

from svgwrite import Drawing
from svgwrite.utils import rgb

LENGTH = 1920
WIDTH = 1080


class Canvas(ICanvas):
    _painter: Drawing
    _center: Point
#в холсте должны быть только те методы, которые есть на схеме

    def __init__(self, file_name: str):
        self._painter = Drawing(file_name, size=(LENGTH, WIDTH))
        self._center = Point(LENGTH / 2, WIDTH / 2)

    def draw_circle(self, center: Point, radius: float, line_color: int) -> None:
        new_center = self._move_origin(center)
        self._painter.add(self._painter.circle(new_center, radius,
                                               stroke=Canvas.convert_int_to_rgb(line_color)))

    def draw_line(self, start_point: Point, end_point: Point, line_color: int) -> None:
        new_start_point = self._move_origin(start_point)
        new_end_point = self._move_origin(end_point)
        self._painter.add(
            self._painter.line(new_start_point, new_end_point, stroke=Canvas.convert_int_to_rgb(line_color)))

    def fill_circle(self, center: Point, radius: float, fill_color: int) -> None:
        new_center = self._move_origin(center)
        self._painter.add(self._painter.circle(new_center, radius, fill=Canvas.convert_int_to_rgb(fill_color)))

    def fill_polygon(self, points: List[Point],  fill_color: int) -> None:
        new_points: List[Tuple[float, float]] = [self._move_origin(point) for point in points]
        self._painter.add(self._painter.polygon(new_points, fill=Canvas.convert_int_to_rgb(fill_color)))

    def save(self):
        self._painter.save()

    def _move_origin(self, point: Point) -> Tuple[float, float]:
        return self.x + point.x, self.y - point.y

    @property
    def x(self) -> float:
        return self._center.x

    @property
    def y(self) -> float:
        return self._center.y

    @staticmethod
    def convert_int_to_rgb(number: int) -> str:
        blue: int = number & 255
        green: int = (number >> 8) & 255
        red: int = (number >> 16) & 255
        return rgb(red, green, blue)
