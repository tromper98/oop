from typing import List

from canvasinterfaces import ICanvas
from point import Point

from svgwrite import Drawing, cm
from svgwrite.utils import rgb

LENGTH = 1920
WIDTH = 1080


class Canvas(ICanvas):
    _painter: Drawing
    _center: Point

    def __init__(self, file_name: str):
        self._painter = Drawing(file_name, size=(LENGTH, WIDTH))
        self._center = Point(WIDTH / 2, LENGTH / 2)

    def draw_circle(self, center: Point, radius: float, line_color: int, fill_color: int) -> None:
        new_center: Point = self._move_origin(center)
        self._painter.add(Drawing.circle(new_center, radius * cm,
                                         stroke=Canvas.convert_int_to_rgb(line_color),
                                         fill=Canvas.convert_int_to_rgb(fill_color)))

    def draw_line(self, start_point: Point, end_point: Point, line_color: int) -> None:
        new_start_point = self._move_origin(start_point)
        new_end_point = self._move_origin(end_point)
        self._painter.add(Drawing.line(new_start_point, new_end_point, stroke=Canvas.convert_int_to_rgb(line_color)))

    def draw_triangle(self, left_up: Point, width: float, length: float, line_color: int, fill_color: int) -> None:
        new_left_up = self._move_origin(left_up)
        self._painter.add(Drawing.rect(new_left_up, (width, length),
                                       stroke=Canvas.convert_int_to_rgb(line_color),
                                       fill=Canvas.convert_int_to_rgb(fill_color)))

    def draw_polygon(self, points: List[Point], line_color: int, fill_color: int) -> None:
        new_points: List[Point] = [self._move_origin(point) for point in points]
        self._painter.add(Drawing.polygon(new_points,
                                          stroke=Canvas.convert_int_to_rgb(line_color),
                                          fill=Canvas.convert_int_to_rgb(fill_color)))

    def save(self):
        self._painter.save()

    def _move_origin(self, point: Point) -> Point:
        return Point(self.x + point.x, self.y + self.y)

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
        return rgb(blue, green, red)
