from .linesegmentimpl import LineSegmentImpl
from point import Point
from canvas.canvasinterfaces import CanvasDrawable, ICanvas


class LineSegment(LineSegmentImpl, CanvasDrawable):
    def __init__(self, start_point: Point, end_point: Point, outline_color: int):
        super().__init__(start_point, end_point, outline_color)

    def get_area(self) -> float:
        return 0

    # Можно вытащить в метод Point.distance_to_point()
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

    def draw(self, canvas: ICanvas):
        canvas.draw_line(self.get_start_point(), self.get_end_point(), self.get_outline_color())
