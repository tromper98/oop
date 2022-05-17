class ShapeException(Exception):
    ...


class InvalidTriangle(ShapeException):
    def __init__(self):
        super().__init__(f'Can\'t create triangle with vertex\'s: '
                         f'more than one vertex have same coords')


class InvalidRectangle(ShapeException):
    def __init__(self):
        super().__init__('Can\'t create rectangle when left top point and right bottom must be different')


class InvalidCircle(ShapeException):
    def __init__(self):
        super().__init__('Can\'t create circle. Radius must be > 0')


class InvalidOutlineColor(ShapeException):
    def __init__(self, number: int):
        super().__init__(f'Invalid outline color number: {number}. Value must integer be in [0, 2^32]')


class InvalidFillColor(ShapeException):
    def __init__(self, number: int):
        super().__init__(f'Invalid fill color number: {number}. Value must be integer in [0, 2^32]')

