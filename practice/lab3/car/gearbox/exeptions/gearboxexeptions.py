from ..gear import Gear


class GearboxException(Exception):
    pass


class InvalidGear(GearboxException):
    def __init__(self, gear_code: int):
        super().__init__(f'Invalid gear. {gear_code} gear not in gearbox')


class InvalidGearSpeed(GearboxException):
    def __init__(self, gear: Gear, speed: float):
        super().__init__(f'Invalid speed {speed} for gear {gear.code}.'
                             f'Speed must be in [{gear.min_speed}, {gear.max_speed}]')


class NeutralGearIncreaseSpeedError(GearboxException):
    def __init__(self):
        super().__init__('Can\'t increase speed on neutral gear')
