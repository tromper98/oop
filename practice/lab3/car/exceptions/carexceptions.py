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


class IncreaseSpeedOnNeutralGearError(CarException):
    def __init__(self):
        super().__init__('Can\'t increase speed in neutral gear')

