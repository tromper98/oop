from shapes.shapeinterfaces import SolidShape
from base.exceptions import InvalidOutlineColor, InvalidFillColor


class BaseShape(SolidShape):
    def __init__(self, outline_color: int, fill_color: int):
        if not SolidShape.is_valid_color_number(outline_color):
            raise InvalidOutlineColor(outline_color)
        if not SolidShape.is_valid_color_number(fill_color):
            raise InvalidFillColor(fill_color)
