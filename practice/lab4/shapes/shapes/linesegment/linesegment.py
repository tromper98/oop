from .linesegmentimpl import LineSegmentImpl
from point import Point
from base.exceptions import InvalidOutlineColor


class LineSegment(LineSegmentImpl):
    _start_point: Point
    _end_point: Point
    _outline_color: int

    def __init__(self, start_point: Point, end_point: Point, outline_color: int):
        super().__init__(start_point, end_point, outline_color)

    def get_area(self) -> float:
        return 0

    #Можно вытащить в метод Point.distance_to_point()
    def get_perimeter(self) -> float:
        return self._start_point.distance_to_point(self._end_point)

    def to_string(self) -> str:
        report: str = f"""
        Line segment
        Start point: {self.get_start_point().to_string}
        End point: {self.get_end_point().to_string}
        Perimeter: {round(self.get_perimeter(), 4)}
        """
        return report

    def get_outline_color(self) -> int:
        return self._outline_color

    def get_start_point(self) -> Point:
        return self._start_point

    def get_end_point(self) -> Point:
        return self._end_point

    @staticmethod
    def is_valid_color_number(number: int) -> bool:
        if 0 <= number <= 2**32:
            return True
        return False
