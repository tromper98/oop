from .RectangleImpl import RectangleImpl
from point import Point


class Rectangle(RectangleImpl):
    def __init__(self, left_top: Point, right_bottom: Point, outline_color: int, fill_color: int):
        #Устранить дублирование кода
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

