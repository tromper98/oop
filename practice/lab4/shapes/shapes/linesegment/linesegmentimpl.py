from base.exceptions import InvalidOutlineColor
from shapes.shapeinterfaces import Shape
from point import Point


class LineSegmentImpl(Shape):
    _start_point: Point
    _end_point: Point
    _outline_color: int

    def __init__(self, start_point: Point, end_point: Point, outline_color: int):
        if not Shape.is_valid_color_number(outline_color):
            raise InvalidOutlineColor(outline_color)

        self._start_point = start_point
        self._end_point = end_point
        self._outline_color = outline_color
