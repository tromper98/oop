import pytest

from base.point import Point
from base.exceptions import *
from shapes import *



def test_circle_to_string():
    center: Point = Point(0, 0)
    circle: Circle = Circle(center, 10, 0, 0)
    expected = """
        Circle
        Center: (0, 0)
        Radius: 10
        Perimeter: 62.8319
        Area: 314.1593
        """
    assert circle.to_string() == expected


def test_rectangle_to_string():
    left_top: Point = Point(1, 4)
    right_bottom: Point = Point(-1, 10)
    rect: Rectangle = Rectangle(left_top, right_bottom, 0, 0)
    expected = """
        Rectangle
        Left top: (1, 4)
        Right top: (-1, 10)
        Perimeter: 16
        Area: 12
        """
    assert rect.to_string() == expected


def test_triangle_to_string():
    vertex1: Point = Point(0, 0)
    vertex2: Point = Point(5, 3)
    vertex3: Point = Point(10, 0)
    triangle: Triangle = Triangle(vertex1, vertex2, vertex3, 0, 0)
    expected = """
        Triangle
        Vertex1: (0, 0)
        Vertex2: (5, 3)
        Vertex3: (10, 0)
        Perimeter: 21.6619
        Area: 15.0
        """
    assert triangle.to_string() == expected


def test_line_segment_to_string():
    start_point: Point = Point(0, 0)
    end_point: Point = Point(10, 10)
    line_segment: LineSegment = LineSegment(start_point, end_point, 0)
    expected = """
        Line segment
        Start point: (0, 0)
        End point: (10, 10)
        Perimeter: 14.1421
        """
    assert line_segment.to_string() == expected


def test_raise_exception_creating_circle():
    start_point: Point = Point(100, 100)
    radius = -100
    with pytest.raises(InvalidCircle):
        Circle(start_point, radius, 10, 10)


def test_raise_exception_creating_rectangle():
    left_top = Point(0, 0)
    right_top = Point(0, 0)
    with pytest.raises(InvalidRectangle):
        Rectangle(left_top, right_top, 10, 10)


def test_raise_exception_creating_triangle():
    vertex1 = Point(0, 0)
    vertex2 = Point(0, 0)
    vertex3 = Point(100, 0)
    with pytest.raises(InvalidTriangle):
        Triangle(vertex1, vertex2, vertex3, 0, 0)


def test_raise_exception_invalid_outline_color_rectangle():
    left_top = Point(5, 5)
    right_bottom = Point(10, 0)
    with pytest.raises(InvalidOutlineColor):
        Rectangle(left_top, right_bottom, -10, 0)


def test_raise_exception_invalid_fill_color_circle():
    center = Point(0, 0)
    radius = 10
    fill_color = 2**32 + 1
    with pytest.raises(InvalidFillColor):
        Circle(center, radius, 10, fill_color)


def test_create_circle_with_max_outline_color_number():
    center = Point(0, 0)
    radius = 10
    fill_color = 2**32
    with pytest.raises(InvalidFillColor):
        Circle(center, radius, 10, fill_color)