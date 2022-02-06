from typing import Optional, Tuple

BORDER = '#'
PASSABLE = ' '
START = 'S'
FINISH = 'F'
ROUTE = '*'


class Cell:
    def __init__(self, x: int, y: int, cell_type: str):
        self.x: int = x
        self.y: int = y
        self.cell_type: str = cell_type
        self.distance: Optional[int] = None
        self.checked: bool = False

    def __str__(self):
        return f'Cell [{self.x}][{self.y}] Distance = {self.distance} Checked = {self.checked}'

    def is_border(self) -> bool:
        return True if self.cell_type == BORDER else False

    def is_start(self) -> bool:
        return True if self.cell_type == START else False

    def is_finish(self) -> bool:
        return True if self.cell_type == FINISH else False

    def is_passable(self) -> bool:
        return True if self.cell_type == PASSABLE else False

    def is_route(self) -> bool:
        return True if self.cell_type == ROUTE else False

    def get_coordinates(self) -> Tuple[int, int]:
        return self.x, self.y

    def get_cell_type(self) -> str:
        if self.is_border():
            return BORDER

        if self.is_start():
            return START

        if self.is_finish():
            return FINISH

        if self.is_passable():
            return PASSABLE

        if self.is_route():
            return ROUTE

        return ''

    def set_route_cell_type(self):
        self.cell_type = ROUTE
