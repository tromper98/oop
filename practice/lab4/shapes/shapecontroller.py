from typing import List, Callable, Dict

from shapes.shapeinterfaces.shape import Shape
from exceptions import ShapeException
from point import Point
from shapes import *


class CommandLineParser:
    _action: str
    _params: List[str]

    def __init__(self, action: str, params: List[str]) -> None:
        self._action = action
        self._params = params

    @property
    def action(self) -> str:
        return self._action

    @property
    def params(self) -> List[str]:
        return self._params

    @staticmethod
    def parse_params(params: List[str]):
        return CommandLineParser(params[0], params[1:])


class ShapeController:
    _shapes: List[Shape]
    _actions: Dict[str, Callable]
    _output: Callable

    def __init__(self, output: Callable = print):
        self._shapes = []
        self._actions = self._init_actions()
        self._output = output

    def execute_command(self, user_input: str) -> bool:
        user_input: str = user_input.lstrip().rstrip()
        parsed_user_input: List[str] = user_input.split(' ')
        parser = CommandLineParser.parse_params(parsed_user_input)

        if self._has_action(parser.action):
            return self._actions[parser.action](parser.params)

        self._output('Invalid command')
        return True

    def _create_rectangle(self, params: List[str]) -> bool:
        if len(params) != 6:
            self._output(f'Need 6 params to create rectangle but {len(params)} params were given')
            return True

        try:
            left_top: Point = Point(float(params[0]), float(params[1]))
            right_bottom: Point = Point(float(params[2]), float(params[3]))
            outline_color: int = int(params[4])
            fill_color: int = int(params[5])
            new_rectangle = Rectangle(left_top, right_bottom, outline_color, fill_color)
            self._shapes.append(new_rectangle)
        except ValueError as e:
            self._output(e)
        except ShapeException as e:
            self._output(e)

        return True

    def _create_circle(self, params: List[str]) -> bool:
        if len(params) != 5:
            self._output(f'Need 5 params to create circle but {len(params)} params were given')
            return True

        try:
            center: Point = Point(float(params[0]), float(params[1]))
            radius: float = float(params[2])
            outline_color: int = int(params[3])
            fill_color: int = int(params[4])
            new_circle = Circle(center, radius, outline_color, fill_color)
            self._shapes.append(new_circle)
        except ValueError as e:
            self._output(e)

        except ShapeException as e:
            self._output(e)

        return True

    def _create_triangle(self, params: List[str]) -> bool:
        if len(params) != 8:
            self._output(f'Need 8 params to create triangle but {len(params)} params were given')
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
            self._output(e)

        except ShapeException as e:
            self._output(e)

        return True

    def _create_line_segment(self, params: List[str]) -> bool:
        if len(params) != 5:
            self._output(f'Need 5 params to create line segment but {len(params)} params were given')
            return True

        try:
            start_point: Point = Point(float(params[0]), float(params[1]))
            end_point: Point = Point(float(params[2]), float(params[3]))
            outline_color: int = int(params[4])
            new_line_segment = LineSegment(start_point, end_point, outline_color)
            self._shapes.append(new_line_segment)
        except ValueError as e:
            self._output(e)

        except ShapeException as e:
            self._output(e)

        return True

    def _print_shape_with_min_perimeter(self, params: List[str]) -> bool:
        if params:
            self._output('Method min_perimeter_shape doesn\'t contains params')
            return True

        if len(self._shapes) == 0:
            self._output('No shapes has been created')
            return True

        shape: Shape = self._get_shape_with_min_perimeter()
        self._output(shape.to_string())
        return True

    def _print_shape_with_max_area(self, params: List[str]) -> bool:
        if params:
            self._output('Method max_area_shape doesn\'t contains params')
            return True

        if len(self._shapes) == 0:
            self._output("No shapes has been created")
            return True

        shape: Shape = self._get_shape_with_max_area()
        self._output(shape.to_string())
        return True

    #Можно упростить поиск минимального/максимального элемента списка
    
    def _get_shape_with_min_perimeter(self) -> Shape:
        min_perimeter_shape = min(self._shapes, key=lambda x: x.get_perimeter())
        return min_perimeter_shape

    def _get_shape_with_max_area(self) -> Shape:
        max_area_shape = max(self._shapes, key=lambda x: x.get_area())
        return max_area_shape

    def _info(self, params: List[str]) -> bool:
        if params:
            self._output('Method max_area_shape doesn\'t contains params')
            return True

        actions: List[str] = [possible_action for possible_action in self._actions.keys()]
        report = f"Possible commands: \n{', '.join(actions)}"
        self._output(report)
        return True

    def _exit(self, params: List[str]) -> bool:
        if params:
            self._output('exit doesn\'t exist params')
            return True

        return False

    def _init_actions(self) -> Dict[str, Callable]:
        actions: Dict[str, Callable] = {
            'rectangle': self._create_rectangle,
            'circle': self._create_circle,
            'triangle': self._create_triangle,
            'line_segment': self._create_line_segment,
            'max_area_shape': self._print_shape_with_max_area,
            'min_perimeter_shape': self._print_shape_with_min_perimeter,
            'info': self._info,
            'exit': self._exit
        }
        return actions

    def _has_action(self, action: str) -> bool:
        return action in [possible_action for possible_action in self._actions.keys()]


def main():
    controller: ShapeController = ShapeController()
    while True:
        cmd: str = input('\nEnter a command: ')
        if not controller.execute_command(cmd):
            break


if __name__ == '__main__':
    main()
