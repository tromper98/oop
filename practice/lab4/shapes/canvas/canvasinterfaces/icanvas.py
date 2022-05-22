from typing import Protocol, List

from point import Point


class ICanvas(Protocol):
    def draw_line(self, start_point: Point, end_point: Point, line_color: int) -> None:
        ...

    def draw_circle(self, center: Point, radius: float, line_color: int) -> None:
        ...

    def fill_polygon(self, points: List[Point], fill_color: int) -> None:
        ...

    def fill_circle(self, center: Point, radius: float, fill_color: int) -> None:
        ...
