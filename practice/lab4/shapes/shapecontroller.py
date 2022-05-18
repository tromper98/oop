from typing import List, Callable, Dict

from base.interfaces.shape import Shape
from base.exceptions import ShapeException
from base.point import Point
from shapes import *


class ShapeController:
    _shapes: List[Shape]
    _actions: Dict[str, Callable]
    _output_print: Callable

    def __init__(self, output_print: Callable = print):
        self._shapes = []
        self._actions = self._init_actions()
        self._output_print = output_print

    def _create_rectangle(self, params: List[str]) -> bool:
        if len(params) != 6:
            self._output_print(f'Need 6 params to create rectangle but {len(params)} params were given')
            return True

        try:
            left_top: Point = Point(float(params[0]), float(params[1]))
            right_bottom: Point = Point(float(params[2]), float(params[3]))
            outline_color: int = int(params[4])
            fill_color: int = int(params[5])
            new_rectangle = Rectangle(left_top, right_bottom, outline_color, fill_color)
            self._shapes.append(new_rectangle)
        except ValueError as e:
            self._output_print(e)
        except ShapeException as e:
            self._output_print(e)

        return True

    def _create_circle(self, params: List[str]) -> bool:
        if len(params) != 5:
            self._output_print(f'Need 5 params to create circle but {len(params)} params were given')
            return True

        try:
            center: Point = Point(float(params[0]), float(params[1]))
            radius: float = float(params[2])
            outline_color: int = int(params[3])
            fill_color: int = int(params[4])
            new_circle = Circle(center, radius, outline_color, fill_color)
            self._shapes.append(new_circle)
        except ValueError as e:
            self._output_print(e)

        except ShapeException as e:
            self._output_print(e)

        return True

    def _create_triangle(self, params: List[str]) -> bool:
        if len(params) != 8:
            self._output_print(f'Need 8 params to create triangle but {len(params)} params were given')
            return True

        try:
            vertex1: Point = Point(float(params[0]), float(params[1]))
            vertex2: Point = Point(float(params[2]), float(params[3]))
            vertex3: Point = Point(float(params[4]), float(params[5]))
            outline_color: int = int(params[6])
            fill_color: int = int(params[7])
            new_triangle = Triangle(vertex1, vertex2, vertex3, outline_color, fill_color)
            self._shapes.append(new_triangle)
        except ValueError as e:
            self._output_print(e)

        except ShapeException as e:
            self._output_print(e)

        return True

    def _create_line_segment(self, params: List[str]) -> bool:
        if len(params) != 8:
            self._output_print(f'Need 5 params to create line segment but {len(params)} params were given')
            return True

        try:
            start_point: Point = Point(float(params[0]), float(params[1]))
            end_point: Point = Point(float(params[2]), float(params[3]))
            outline_color: int = int(params[4])
            new_line_segment = LineSegment(start_point, end_point, outline_color)
            self._shapes.append(new_line_segment)
        except ValueError as e:
            self._output_print(e)

        except ShapeException as e:
            self._output_print(e)

        return True

    def _get_shape_with_min_perimeter(self):
        ...

    def _get_shape_with_max_area(self):
        ...

    def _exit(self, params: List[str]) -> bool:
        if params:
            self._output_print('exit doesn\'t exist params')
            return True

        return False

    def _init_actions(self) -> Dict[str, Callable]:
        actions: Dict[str, Callable] = {
            'rectangle': self._create_rectangle,
            'circle': self._create_circle,
            'triangle': self._create_triangle,
            'line_segment': self._create_line_segment,
            'max_area_shape': self._get_shape_with_max_area,
            'min_perimeter_shape': self._get_shape_with_min_perimeter,
            'exit': self._exit
        }
        return actions
