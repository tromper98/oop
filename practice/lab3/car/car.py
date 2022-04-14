from typing import List, Tuple, Optional
from gearbox import Gearbox


class Car:
    _speed: float
    _gearbox: Gearbox
    _engine: bool
    _direction: int

    def __init__(self):
        self._speed = 0
        self._gearbox = Gearbox()
        self._engine = False
        self._direction = 0

    def _update_direction(self) -> None:
        if self._speed == 0:
            self._direction = 0
            return

        if self._speed > 0 and self._gearbox.is_reverse_gear:
            self._direction = -1
            return

        self._direction = 1

    def engine_on(self) -> bool:
        if not self._engine:
            self._engine = True
        return True

    def engine_off(self) -> bool:
        if not self._engine:
            return True

        if self._engine and self._gearbox.is_neutral_gear and self._speed == 0:
            self._engine = False
            return True

        return False

    def set_gear(self, new_gear: int) -> bool:
        is_turned: bool = self._gearbox.change_gear(self._speed, new_gear)
        self._update_direction()

        if not is_turned:
            return False
        return True

    def set_speed(self, new_speed: float) -> True:
        if self._gearbox.is_neutral_gear:
            if new_speed <= self._speed:
                self._speed = new_speed
                return True

            return False

        min_speed: float = self._gearbox.gear.min_speed
        max_speed: float = self._gearbox.gear.max_speed

        if min_speed <= new_speed <= max_speed:
            self._speed = new_speed
            self._update_direction()
            return True

        return False

    @property
    def is_turned_on(self) -> bool:
        return self._engine

    @property
    def direction(self) -> str:
        if self._direction == 1:
            return 'Forward'
        if self._direction == -1:
            return 'Reverse'
        return 'Stop'

    @property
    def speed(self) -> float:
        return abs(self._speed)

    @property
    def gear(self) -> int:
        return self._gearbox.gear.code

    def info(self) -> None:
        report: str = f"""
        --- Car Info ---
        Engine: {'On' if self.is_turned_on else 'Off'}
        Direction: {self.direction}
        Speed: {self.speed}
        Gear: {self.gear}
        --- End Car Info ---
        """
        print(report)


def exec_action(car: Car, action: str, param: int) -> None:
    if action == 'info':
        car.info()
        return

    if action == 'engineOn':
        result: bool = car.engine_on()
        return

    if action == 'engineOff':
        result = car.engine_off()
        return

    if action == 'setSpeed':
        result = car.set_speed(param)
        return

    if action == 'setGear':
        result = car.set_gear(param)
        return


def parse_action(action: str) -> Optional[Tuple[str, Optional[int]]]:
    parsed_action: List[str] = action.split(' ')
    if len(parsed_action) > 2:
        print('Too much parameters were given')
        return None

    if len(parsed_action) == 1:
        return parsed_action[0], None

    try:
        param: int = int(parsed_action[1])
    except ValueError:
        print('Action parameter must be a number')
        return None

    return parsed_action[0], param


def validate_action(action: str, param: Optional[int], parametrize_action: List[str]) -> bool:
    if action not in parametrize_action:
        return True

    if param is not None:
        return True

    print(f'Invalid parameter: {param} for {action}')
    return False


def get_action(actions: List[str]) -> Tuple[str, Optional[int]]:
    while True:
        print(f'Choose one command: {", ".join(actions)}')
        user_input: str = input(f'Enter a command for car: ').lstrip().rstrip()
        action, param = parse_action(user_input)

        if action in actions:
            break

        print('Invalid command')

    return action, param


def main():
    actions: List[str] = ['info', 'engineOn', 'engineOff', 'setSpeed', 'setGear', 'exit']
    parametrize_actions: List[str] = ['setSpeed', 'setGear']
    car: Car = Car()
    while True:
        action, param = get_action(actions)

        if action == 'exit':
            break

        if validate_action(action, param, parametrize_actions):
            exec_action(car, action, param)


if __name__ == '__main__':
    main()
