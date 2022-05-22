from typing import List

from .RectangleImpl import RectangleImpl
from point import Point
from canvas.canvasinterfaces import CanvasDrawable, ICanvas


class Rectangle(RectangleImpl, CanvasDrawable):
    def __init__(self, left_top: Point, right_bottom: Point, outline_color: int, fill_color: int):
        # Устранить дублирование кода
        super().__init__(left_top, right_bottom, outline_color, fill_color)

    def get_height(self) -> float:
        return abs(self._left_top.y - self._right_bottom.y)

    def get_width(self) -> float:
        return abs(self._left_top.x - self._right_bottom.x)

    def get_perimeter(self) -> float:
        height: float = self.get_height()
        width: float = self.get_width()
        return 2 * (height + width)

    def get_area(self) -> float:
        height: float = self.get_height()
        width: float = self.get_width()
        return height * width

    def to_string(self) -> str:
        report = f"""
        Rectangle
        Left top: {self.get_left_top().to_string}
        Right top: {self.get_right_bottom().to_string}
        Perimeter: {round(self.get_perimeter(), 4)}
        Area: {round(self.get_area(), 4)}
        """
        return report

    def get_outline_color(self) -> int:
        return self._outline_color

    def get_fill_color(self) -> int:
        return self._fill_color

    def get_left_top(self) -> Point:
        return self._left_top

    def get_right_bottom(self) -> Point:
        return self._right_bottom

    def draw(self, canvas: ICanvas):
        right_top: Point = Point(self.get_right_bottom().x, self.get_left_top().y)
        left_bottom: Point = Point(self.get_left_top().x, self.get_right_bottom().y)

        points: List[Point] = [self.get_left_top(), right_top, self.get_right_bottom(), left_bottom]

        canvas.draw_line(self.get_left_top(), right_top, self.get_outline_color())
        canvas.draw_line(right_top, self.get_right_bottom(), self.get_outline_color())
        canvas.draw_line(self.get_right_bottom(), left_bottom, self.get_outline_color())
        canvas.draw_line(left_bottom, self.get_left_top(), self.get_outline_color())

        canvas.fill_polygon(points, self.get_fill_color())
