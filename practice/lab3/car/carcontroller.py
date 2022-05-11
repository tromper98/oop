from typing import List, Union, Callable, Dict, Optional
from car import Car
from exceptions import CarException


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

    # Лучше передать car передавать снаружи
    def __init__(self, car: Car):
        self._car = car
        self._actions: Dict[str, Callable] = self._get_actions()

    def execute_command(self, user_input: str) -> Optional[bool]:
        user_input: str = user_input.lstrip().rstrip()
        parsed_user_input: List[str] = user_input.split(' ')
        parser = CommandLineParser.parse_params(parsed_user_input)

        if self._has_action(parser.action):
            return self._actions[parser.action](parser.params)

        print('Inlavid command')

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

    def _get_help(self, params) -> None:
        if params:
            print('Action "help" doesn\'t exists params')
            return

        action_list: List[str] = [action for action in self._actions.keys()]
        output: str = ' '.join(action_list)
        print(output)

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
            print('Action "setSpeed" have one parameter - speed: float')
            return

        new_speed: float = CarController._convert_string_to_number(params[0])
        try:
            self._car.set_speed(new_speed)
        except CarException as e:
            print(e)

    def _set_gear(self, params: List[str]) -> None:
        if len(params) != 1:
            print('Action "setGear" have one parameter - gear_code: int')
            return

        new_gear: int = CarController._convert_string_to_number(params[0])
        try:
            self._car.set_gear(new_gear)
        except CarException as e:
            print(e)

    def _exit(self, params: List[str]) -> Optional[bool]:
        if params:
            print('Action "exit" doesn\'t exists params')
            return

        return True

    def _get_actions(self) -> Dict[str, Callable]:
        actions: Dict[str, Callable] = {
            'help': self._get_help,
            'info': self._get_car_info,
            'engineOn': self._engine_on,
            'engineOff': self._engine_off,
            'setSpeed': self._set_speed,
            'setGear': self._set_gear,
            'exit': self._exit
        }
        return actions

    def _has_action(self, searchable_action: str) -> bool:
        return searchable_action in [action for action in self._actions.keys()]

    @staticmethod
    def _convert_string_to_number(string: str) -> Union[int, float]:
        try:
            return int(string)
        except ValueError:
            print(f'{string} is not a number')


def main():
    car = Car()
    car_controller: CarController = CarController(car)
    while True:
        cmd: str = input('\nEnter a command for car: ')
        if car_controller.execute_command(cmd):
            break


if __name__ == '__main__':
    main()

# cc = CarController(car, test_print)
# assert cc.execute_command("setGear 3")
#
#
# while True
#     cmd = input("Enter command: ")
#     if not cc.execute_command(cmd):
#         break
#
# prompt = ""
# def my_input(s):
#     prompt = s
#     yield "Info"
#     prompt = s
#     yield "EngineOn"
#     yield "SetGear 1"
#
# cc = CarController(car, my_input, my_output)
# cc.execute_command()
# assert prompt == "Enter command: "
# assert
