class CarException(Exception):
    pass


class EngineOnError(CarException):
    def __init__(self):
        super().__init__('Can\'t turn on engine. You can turn on engine only on neutral and speed = 0')


class EngineOffError(CarException):
    def __init__(self):
        super().__init__('Can\'t turn off engine. You can turn off engine only on speed = 0 and neutral')


class GearSwitchingEngineOffError(CarException):
    def __init__(self):
        super().__init__('Can\'t change gear when engine turned off')


class ChangeSpeedOnNeutralGearError(CarException):
    def __init__(self, speed: float):
        super().__init__(f'Can\'t set speed to {speed} in neutral gear')


class CarSpeedError(CarException):
    def __init__(self, min_speed: float, max_speed: float):
        maximum_speed = max((abs(min_speed), abs(max_speed)))
        minimum_speed = min((abs(min_speed), abs(max_speed)))
        super().__init__(f'Can\'t change speed beyond gear limits [{minimum_speed}, {maximum_speed}]')


class CarChangeSpeedOnEngineOff(CarException):
    def __init__(self):
        super().__init__(f'Can\'t change speed if engine off')


class InvalidGear(CarException):
    def __init__(self, gear_code: int):
        super().__init__(f'Invalid gear. {gear_code} gear not in gearbox')


class InvalidGearSpeed(CarException):
    def __init__(self, gear, speed: float):
        super().__init__(f'Invalid speed {speed} for gear {gear.code}.'
                         f'Speed must be in [{gear.min_speed}, {gear.max_speed}]')


class NeutralGearIncreaseSpeedError(CarException):
    def __init__(self):
        super().__init__('Can\'t increase speed on neutral gear')
