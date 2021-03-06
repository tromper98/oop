import pytest
from unittest import TestCase

from svgwrite import Drawing, rgb

from point import Point
from exceptions import *
from shapes import *

from canvas import Canvas
from shapecontroller import ShapeController

OUTPUT_STORAGE = []


def is_equal_rectangle(target: Rectangle, expected: Rectangle) -> bool:
    if target.get_left_top() != expected.get_left_top():
        return False

    if target.get_right_bottom() != expected.get_right_bottom():
        return False

    if target.get_fill_color() != expected.get_fill_color():
        return False

    if target.get_outline_color() != expected.get_outline_color():
        return False

    if target.get_perimeter() != expected.get_perimeter():
        return False

    if target.get_area() != expected.get_area():
        return False

    return True


def is_equal_circle(target: Circle, expected: Circle):
    if target.get_center() != expected.get_center():
        return False

    if target.get_radius() != expected.get_radius():
        return False

    if target.get_fill_color() != expected.get_fill_color():
        return False

    if target.get_outline_color() != expected.get_outline_color():
        return False

    if target.get_perimeter() != expected.get_perimeter():
        return False

    if target.get_area() != expected.get_area():
        return False

    return True


def is_equal_triangle(target: Triangle, expected: Triangle) -> bool:
    if target.get_vertex1() != expected.get_vertex1():
        return False

    if target.get_vertex2() != expected.get_vertex2():
        return False

    if target.get_vertex3() != expected.get_vertex3():
        return False

    if target.get_fill_color() != expected.get_fill_color():
        return False

    if target.get_outline_color() != expected.get_outline_color():
        return False

    if target.get_perimeter() != expected.get_perimeter():
        return False

    if target.get_area() != expected.get_area():
        return False

    return True


def is_equal_line_segment(target: LineSegment, expected: LineSegment) -> bool:
    if target.get_start_point() != expected.get_start_point():
        return False

    if target.get_end_point() != expected.get_end_point():
        return False

    if target.get_outline_color() != expected.get_outline_color():
        return False

    if target.get_perimeter() != expected.get_perimeter():
        return False

    if target.get_area() != expected.get_area():
        return False

    return True


def assert_equal_drawing(target: Drawing, expected: Drawing):
    compared_shapes = tuple(zip(target.elements, expected.elements))
    for i in range(1, len(compared_shapes)):
        shapes = compared_shapes[i]
        target_element, expected_element = shapes[0], shapes[1]
        target_attrs = target_element.attribs
        expected_attrs = expected_element.attribs
        assert target_attrs == expected_attrs


def convert_hex_to_rgb(number: str) -> str:
    number = int(number, 16)
    blue: int = number & 255
    green: int = (number >> 8) & 255
    red: int = (number >> 16) & 255
    return rgb(red, green, blue)


def write_to_output_storage(string: str):
    return OUTPUT_STORAGE.append(string)


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
    Circle(center, radius, 10, fill_color)


def test_create_rectangle_from_shape_controller():
    controller: ShapeController = ShapeController(write_to_output_storage)
    action = 'rectangle'
    params = ['0', '10', '100', '0', '15', '20']
    controller.execute_command(action + ' ' + ' '.join(params))
    expected = Rectangle(Point(0, 10), Point(100, 0), int('15', 16), int('20', 16))
    assert is_equal_rectangle(controller._shapes[0], expected)


def test_create_circle_from_shape_controller():
    controller: ShapeController = ShapeController(write_to_output_storage)
    action = 'circle'
    params = ['10', '-15', '100.5', '40', '100']
    controller.execute_command(action + ' ' + ' '.join(params))
    expected = Circle(Point(10, -15), 100.5, int('40', 16), int('100', 16))
    assert is_equal_circle(controller._shapes[0], expected)


def test_create_triangle_from_shape_controller():
    controller: ShapeController = ShapeController(write_to_output_storage)
    action = 'triangle'
    params = ['0', '0', '10', '10', '20', '-50', '50', '30']
    controller.execute_command(action + ' ' + ' '.join(params))
    expected = Triangle(Point(0, 0), Point(10, 10), Point(20, -50), int('50', 16), int('30', 16))
    assert is_equal_triangle(controller._shapes[0], expected)


def test_create_line_segment_from_shape_controller():
    controller: ShapeController = ShapeController(write_to_output_storage)
    action = 'line_segment'
    params = ['0', '0', '100', '200', '36']
    controller.execute_command(action + ' ' + ' '.join(params))
    expected = LineSegment(Point(0, 0), Point(100, 200), int('36', 16))
    assert is_equal_line_segment(controller._shapes[0], expected)


def test_fail_create_rectangle_with_not_enough_params():
    OUTPUT_STORAGE.clear()
    controller: ShapeController = ShapeController(write_to_output_storage)
    action = 'rectangle'
    params = ['41', '42', '5', '3']
    controller.execute_command(action + ' ' + ' '.join(params))
    expected = 'Need 6 params to create rectangle but 4 params were given'
    assert OUTPUT_STORAGE[0] == expected


def test_fail_create_rectangle_with_invalid_params():
    OUTPUT_STORAGE.clear()
    controller: ShapeController = ShapeController(write_to_output_storage)
    action = 'rectangle'
    params = ['41', '42', '5', '3', '??????????', '??????????????']
    controller.execute_command(action + ' ' + ' '.join(params))
    expected = "invalid literal for int() with base 16: '??????????'"
    assert OUTPUT_STORAGE[0].args[0] == expected


def test_fail_create_circle_with_not_enough_params():
    OUTPUT_STORAGE.clear()
    controller: ShapeController = ShapeController(write_to_output_storage)
    action = 'circle'
    params = ['100', '100', '2000']
    controller.execute_command(action + ' ' + ' '.join(params))
    expected = 'Need 5 params to create circle but 3 params were given'
    assert OUTPUT_STORAGE[0] == expected


def test_fail_create_circle_with_invalid_params():
    OUTPUT_STORAGE.clear()
    controller: ShapeController = ShapeController(write_to_output_storage)
    action = 'circle'
    params = ['x1', 'x2', '5', '3', '10']
    controller.execute_command(action + ' ' + ' '.join(params))
    expected = "could not convert string to float: 'x1'"
    assert OUTPUT_STORAGE[0].args[0] == expected


def test_fail_create_triangle_with_not_enough_params():
    OUTPUT_STORAGE.clear()
    controller: ShapeController = ShapeController(write_to_output_storage)
    action = 'triangle'
    params = ['0', '0', '10', '19', '35', '49']
    controller.execute_command(action + ' ' + ' '.join(params))
    expected = 'Need 8 params to create triangle but 6 params were given'
    assert OUTPUT_STORAGE[0] == expected


def test_fail_create_triangle_with_invalid_params():
    OUTPUT_STORAGE.clear()
    controller: ShapeController = ShapeController(write_to_output_storage)
    action = 'triangle'
    params = ['0', '0', 'vertex2', 'vertex2', '10', '10', '3', '8']
    controller.execute_command(action + ' ' + ' '.join(params))
    expected = "could not convert string to float: 'vertex2'"
    assert OUTPUT_STORAGE[0].args[0] == expected


def test_fail_create_line_segment_with_not_enough_params():
    OUTPUT_STORAGE.clear()
    controller: ShapeController = ShapeController(write_to_output_storage)
    action = 'line_segment'
    params = ['0', '0', '10', '19', '35', '49']
    controller.execute_command(action + ' ' + ' '.join(params))
    expected = f'Need 5 params to create line segment but {len(params)} params were given'
    assert OUTPUT_STORAGE[0] == expected


def test_fail_create_line_segment_with_invalid_params():
    OUTPUT_STORAGE.clear()
    controller: ShapeController = ShapeController(write_to_output_storage)
    action = 'line_segment'
    params = ['0', '0', '10', '100', 'color']
    controller.execute_command(action + ' ' + ' '.join(params))
    expected = "invalid literal for int() with base 16: 'color'"
    assert OUTPUT_STORAGE[0].args[0] == expected


def test_call_print_min_perimeter_shape_with_params():
    OUTPUT_STORAGE.clear()
    controller: ShapeController = ShapeController(write_to_output_storage)
    action = 'min_perimeter_shape'
    params = ['a', 'b', 'c', 'd']
    controller.execute_command(action + ' ' + ' '.join(params))
    expected = 'Method "min_perimeter_shape" doesn\'t contains params'
    assert OUTPUT_STORAGE[0] == expected


def test_call_print_min_perimeter_without_shapes():
    OUTPUT_STORAGE.clear()
    controller: ShapeController = ShapeController(write_to_output_storage)
    action = 'min_perimeter_shape'
    controller.execute_command(action)
    expected = 'No shapes has been created'
    assert OUTPUT_STORAGE[0] == expected


def test_call_print_max_area_shape_with_params():
    OUTPUT_STORAGE.clear()
    controller: ShapeController = ShapeController(write_to_output_storage)
    action = 'max_area_shape'
    params = ['a', 'b', 'c', 'd']
    controller.execute_command(action + ' ' + ' '.join(params))
    expected = 'Method "max_area_shape" doesn\'t contains params'
    assert OUTPUT_STORAGE[0] == expected


def test_call_print_max_area_without_shapes():
    OUTPUT_STORAGE.clear()
    controller: ShapeController = ShapeController(write_to_output_storage)
    action = 'max_area_shape'
    controller.execute_command(action)
    expected = 'No shapes has been created'
    assert OUTPUT_STORAGE[0] == expected


def test_get_max_area_shape_from_some_shapes():
    OUTPUT_STORAGE.clear()
    input_file: str = './data/shapes1.txt'
    controller: ShapeController = ShapeController(write_to_output_storage)
    with open(input_file, 'r', encoding='utf-8') as file:
        for row in file:
            controller.execute_command(row)
    expected = Rectangle(Point(1000.0, 56.0), Point(30.0, 5.0), 7, 1)
    controller.execute_command('max_area_shape')
    assert OUTPUT_STORAGE[0] == expected.to_string()


def test_get_min_perimeter_shape_from_some_shapes():
    OUTPUT_STORAGE.clear()
    input_file: str = './data/shapes1.txt'
    controller: ShapeController = ShapeController(write_to_output_storage)
    with open(input_file, 'r', encoding='utf-8') as file:
        for row in file:
            controller.execute_command(row)
    expected = Rectangle(Point(0.0, 0.0), Point(-10.0, 5.0), 24, 4)
    controller.execute_command('min_perimeter_shape')
    assert OUTPUT_STORAGE[0] == expected.to_string()


@pytest.mark.skip()
def test_draw_fir_tree():
    OUTPUT_STORAGE.clear()
    input_file: str = './data/tree.txt'
    controller: ShapeController = ShapeController(write_to_output_storage)
    with open(input_file, 'r', encoding='utf-8') as file:
        for row in file:
            controller.execute_command(row)
    controller.execute_command('draw_shapes ./data/tree.svg')


def test_draw_line():
    OUTPUT_STORAGE.clear()
    controller = ShapeController(write_to_output_storage)
    mock_canvas = Canvas('./data/test/svg')
    cmd = 'line_segment -200 200 400 500 F0FFF0'

    controller.execute_command(cmd)

    expected = Drawing(size=(1920, 1080))
    expected.add(expected.line((760.0, 340.0), (1360.0, 40.0), stroke=convert_hex_to_rgb('F0FFF0')))
    assert_equal_drawing(controller._draw_shapes_on_canvas(mock_canvas)._painter, expected)


def test_draw_circle():
    OUTPUT_STORAGE.clear()
    controller = ShapeController(write_to_output_storage)
    mock_canvas = Canvas('./data/test/svg')
    cmd = 'circle 0 0 250 87CEFA FA4600'

    controller.execute_command(cmd)

    expected = Drawing(size=(1920, 1080))
    expected.add(expected.circle((960, 540), 250, stroke=convert_hex_to_rgb('87CEFA')))
    expected.add(expected.circle((960, 540), 250, fill=convert_hex_to_rgb('FA4600')))
    assert_equal_drawing(controller._draw_shapes_on_canvas(mock_canvas)._painter, expected)


def test_draw_rectangle():
    OUTPUT_STORAGE.clear()
    controller = ShapeController(write_to_output_storage)
    mock_canvas = Canvas('./data/test/svg')
    cmd = 'rectangle -300 0 450 -200 9ACD32 00FFFF'

    controller.execute_command(cmd)

    expected = Drawing(size=(1920, 1080))
    expected.add(expected.line((660, 540), (1410, 540), stroke=convert_hex_to_rgb('9ACD32')))
    expected.add(expected.line((1410, 540), (1410, 740), stroke=convert_hex_to_rgb('9ACD32')))
    expected.add(expected.line((1410, 740), (660, 740), stroke=convert_hex_to_rgb('9ACD32')))
    expected.add(expected.line((660, 740), (660, 540), stroke=convert_hex_to_rgb('9ACD32')))
    expected.add(expected.polygon(((640, 540), (1410, 540), (1410, 740), (660, 740)),
                                  fill=convert_hex_to_rgb('00FFFF')))

    assert_equal_drawing(controller._draw_shapes_on_canvas(mock_canvas)._painter, expected)


def test_draw_triangle():
    OUTPUT_STORAGE.clear()
    controller = ShapeController(write_to_output_storage)
    mock_canvas = Canvas('./data/test/svg')
    cmd = 'triangle -200 -200 -200 500 400 0 87CEFA DEB887'

    controller.execute_command(cmd)

    expected = Drawing(size=(1920, 1080))
    expected.add(expected.line((760, 740), (760, 40), stroke=convert_hex_to_rgb('87CEFA')))
    expected.add(expected.line((760, 40), (1360, 540), stroke=convert_hex_to_rgb('87CEFA')))
    expected.add(expected.line((1360, 540), (760, 740), stroke=convert_hex_to_rgb('87CEFA')))
    expected.add(expected.polygon(((760, 740), (760, 40), (1360, 540)), fill=convert_hex_to_rgb('DEB887')))

    assert_equal_drawing(controller._draw_shapes_on_canvas(mock_canvas)._painter, expected)
