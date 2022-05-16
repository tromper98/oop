from ..point import Point


class ShapeException(Exception):
    ...


class InvalidTriangle(ShapeException):
    def __init__(self, vertex1: Point, vertex2: Point, vertex3: Point):
        super().__init__(f'Can\'t creata triangle with vertex\'s: '
                         f'{vertex1.to_string}. {vertex2.to_string}, {vertex3.to_string}')
