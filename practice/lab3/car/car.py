from typing import Tuple
from gearbox import *
from gearbox.gear import NEUTRAL_GEAR_CODE
from exceptions import *

STOP: str = 'Stop'
REVERSE_DIRECTION: str = 'Reverse'
FORWARD_DIRECTION: str = 'Forward'


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

        if self._speed < 0:
            self._direction = -1
            return

        self._direction = 1

    # Класс не должен заниматься вводом/выводом
    def engine_on(self) -> None:
        if not self._gearbox.is_on_neutral_gear or self._speed != 0:
            raise EngineOnError()

        self._engine = True

    def engine_off(self) -> None:
        if self._engine and self._gearbox.is_on_neutral_gear and self._speed == 0:
            self._engine = False
            return

        raise EngineOffError()

    def set_gear(self, new_gear: int) -> None:
        if not self.is_engine_on and new_gear != NEUTRAL_GEAR_CODE:
            raise GearSwitchingEngineOffError()

        self._gearbox.change_gear(self._speed, new_gear)
        self._update_direction()

    def set_speed(self, new_speed: float) -> None:

        if not self.is_engine_on:
            raise CarChangeSpeedOnEngineOff()
        if self._gearbox.is_on_neutral_gear:
            min_speed, max_speed = Car._shuffle_min_max_speed(0, self._speed)
            if not (min_speed <= new_speed * self._direction <= max_speed):
                raise ChangeSpeedOnNeutralGearError(new_speed)

            self._speed = new_speed * self._direction
            self._update_direction()
            return

        if self._gearbox.is_on_reverse_gear:
            new_speed = -new_speed

        min_speed, max_speed = Car._shuffle_min_max_speed(self._gearbox.gear.min_speed, self._gearbox.gear.max_speed)
        if min_speed <= new_speed <= max_speed:
            self._speed = new_speed
            self._update_direction()
            return

        raise CarSpeedError(min_speed, max_speed)

    @property
    def is_engine_on(self) -> bool:
        return self._engine

    # Лучше возвращать константы
    @property
    def direction(self) -> str:
        if self._direction == 1:
            return FORWARD_DIRECTION
        if self._direction == -1:
            return REVERSE_DIRECTION
        return STOP

    @property
    def speed(self) -> float:
        return abs(self._speed)

    @property
    def gear(self) -> int:
        return self._gearbox.gear.code

    @staticmethod
    def _shuffle_min_max_speed(min_speed: float, max_speed: float) -> Tuple[float, float]:
        return min((min_speed, max_speed)), max(min_speed, max_speed)
