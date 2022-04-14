from typing import List, Tuple, Optional
from .gearbox import Gearbox


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

        if self._speed > 0 and self._gearbox.is_reverse_gear:
            self._direction = -1

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

    def info(self) -> str:
        report: str = f"""
        --- Car Info ---
        Engine: {'On' if self.is_turned_on else 'Off'}
        Direction: {self.direction}
        Speed: {self.speed}
        Gear: {self.gear}
        --- End Car Info ---
        """
        return report


def parse_action(action: str) -> Optional[Tuple[str, int]]:
    parsed_action: List[str] = action.split(' ')
    if len(parsed_action) > 2:
        print('Too much parameters were given')
        return None

    if not parsed_action[2].isdigit():
        print('Action parameter must be a number')
        return None
    return parsed_action[0], int(parsed_action[1])


def exec_action(car: Car, action: str, param: int) -> None:
    if action == 'info':
        car.info()
        return

    if action == 'engine on':
        car.engine_on()
        return

    if action == 'engine off':
        car.engine_off()
        return

    if action == 'set speed':
        car.set_speed(param)

    if action == 'set gear':
        car.set_gear(param)


def get_action(actions: List[str]) -> str:
    action: str = ''
    while action not in actions:
        action = input('Enter a command for car: ')

    return action.lstrip().rstrip()


def main():
    actions: List[str] = ['info', 'engineOn', 'engineOff', 'setSpeed', 'setGear', 'exit']
    car = Car()
    user_input = ''
    while user_input:
        user_input = get_action(actions)
        action, param = parse_action(user_input)

        if action == 'exit':
            break

        exec_action(car, action, param)


if __name__ == '__main__':
    main()