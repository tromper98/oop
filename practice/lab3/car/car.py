from typing import List, Tuple, Optional
from gearbox import Gearbox

ACTIONS: List[str] = ['info', 'engineOn', 'engineOff', 'setSpeed', 'setGear', 'exit']


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

#Класс не должен заниматься вводом/выводом
    def engine_on(self) -> bool:
        if not self._gearbox.is_neutral_gear or self._speed != 0:
            print('Can\'t turn on engine. You can turn on engine only on neutral and speed = 0')
            return False

        self._engine = True
        return True

    def engine_off(self) -> bool:
        if self._engine and self._gearbox.is_neutral_gear and self._speed == 0:
            self._engine = False
            return True

        print('Can\'t turn off engine. You can turn off engine only on speed = 0 and neutral')
        return False

    def set_gear(self, new_gear: int) -> bool:
        if not self.is_engine_on:
            print('Can\'t change gear when engine turned off')
            return False

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

            print('Can\'t increase speed in neutral gear')
            return False

        min_speed: float = self._gearbox.gear.min_speed
        max_speed: float = self._gearbox.gear.max_speed

        if min_speed <= new_speed <= max_speed:
            self._speed = new_speed
            self._update_direction()
            return True

        print(f'Can\'t change speed beyond gear limits [{min_speed}, {max_speed}]')
        return False

    @property
    def is_engine_on(self) -> bool:
        return self._engine

#Лучше возвращать константы
    @property
    def direction(self) -> str:
        if self._direction == 1:
            return 'Forward'
        if self._direction == -1:
            return 'Reverse'
        return 'Stop'

    @property
    def speed(self) -> float:
        return self._speed

    @property
    def gear(self) -> int:
        return self._gearbox.gear.code

#Должен возвращать класс, занимающийся вводом/выводом
    def info(self) -> None:
        report: str = f"""
        --- Car Info ---
        Engine: {'On' if self.is_engine_on else 'Off'}
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
        car.engine_on()
        return

    if action == 'engineOff':
        car.engine_off()
        return

    if action == 'setSpeed':
        car.set_speed(param)
        return

    if action == 'setGear':
        car.set_gear(param)
        return

#Tuple
def parse_action(action: str) -> Tuple[Optional[str], Optional[int]]:
    parsed_action: List[str] = action.split(' ')
    if len(parsed_action) > 2:
        print('Too much parameters were given')
        return None, None

    if len(parsed_action) == 1:
        return parsed_action[0], None

    try:
        int(parsed_action[1])
    except ValueError:
        print('action param must be a number')
        return None, None

    return parsed_action[0], int(parsed_action[1])


def get_action() -> Tuple[str, Optional[int]]:
    while True:
        print(f'Choose one command: {", ".join(ACTIONS)}')
        user_input: str = input(f'\nEnter a command for car: ').lstrip().rstrip()
        action, param = parse_action(user_input)

        if action in ACTIONS:
            break

        print('Invalid command')

    return action, param


def main():
    car: Car = Car()
    while True:
        action, param = get_action()

        if action == 'exit':
            break

        exec_action(car, action, param)


if __name__ == '__main__':
    main()
