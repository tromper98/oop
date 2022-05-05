from typing import List, Union, Callable
from car import Car
from exceptions import CarException

ACTIONS: List[str] = ['info', 'engineOn', 'engineOff', 'setSpeed', 'setGear', 'exit']


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


class CarController:
    _car: Car

    def __init__(self) -> None:
        self._car = Car()

    def execute_command(self, action: str, params: List[str]) -> None:
        if action == 'info':
            self._get_car_info(params)
            return

        if action == 'engineOn':
            self._engine_on(params)
            return

        if action == 'engineOff':
            self._engine_off(params)
            return

        if action == 'setSpeed':
            self._set_speed(params)
            return

        if action == 'setGear':
            self._set_gear(params)
            return

    # Должен возвращать класс, занимающийся вводом/выводом
    def _get_car_info(self, params: List[str]) -> None:
        if params:
            print('Action "info" doesn\'t exists params')
            return

        report: str = f"""
        --- Car Info ---
        Engine: {'On' if self._car.is_engine_on else 'Off'}
        Direction: {self._car.direction}
        Speed: {self._car.speed}
        Gear: {self._car.gear}
        --- End Car Info ---
        """
        print(report)

    def _engine_on(self, params: List[str]) -> None:
        if params:
            print('Action "engineOn" doesn\'t exists params')
            return

        try:
            self._car.engine_on()
        except CarException as e:
            print(e)

    def _engine_off(self, params: List[str]) -> None:
        if params:
            print('Action "engineOff" doesn\'t exists params')
            return

        try:
            self._car.engine_off()
        except CarException as e:
            print(e)

    def _set_speed(self, params: List[str]) -> None:
        if len(params) != 1:
            print('Action "setSpeed" have only one parameter')
            return

        new_speed: float = CarController._convert_string_to_number(params[0])
        try:
            self._car.set_speed(new_speed)
        except CarException as e:
            print(e)

    def _set_gear(self, params: List[str]) -> None:
        if len(params) != 1:
            print('Action "setGear" have only one parameter')
            return

        new_gear: int = CarController._convert_string_to_number(params[0])
        try:
            self._car.set_gear(new_gear)
        except CarException as e:
            print(e)


    @staticmethod
    def _convert_string_to_number(string: str) -> Union[int, float]:
        try:
            return int(string)
        except ValueError:
            print(f'{string} is not a number')


def get_user_input() -> List[str]:
    while True:
        print(f'Choose command: {", ".join(ACTIONS)}')
        user_input: str = input(f'\nEnter a command for car: ').lstrip().rstrip()
        parsed_user_input: List[str] = user_input.split(' ')
        if parsed_user_input[0] in ACTIONS:
            break

        print('Invalid command')

    return parsed_user_input


def main():
    car_controller: CarController = CarController()
    while True:
        user_input: List[str] = get_user_input()
        parser = CommandLineParser.parse_params(user_input)

        if parser.action == 'exit':
            break

        car_controller.execute_command(parser.action, parser.params)


if __name__ == '__main__':
    main()

