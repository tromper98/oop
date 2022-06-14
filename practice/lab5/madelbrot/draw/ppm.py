from typing import List, Tuple

from rgb import RGB

FORMAT = 'P6'


class PPMImage:
    _file_name: str
    _columns: int
    _rows: int
    _brightness: int

    def __init__(self, file_name: str, columns: int, rows: int, brightness: int = 1):
        if not 1 <= brightness <= 255:
            raise ValueError('Brightness must be in [1, 255]')

        self._file_name = file_name
        self._columns = columns
        self._rows = rows
        self._brightness = brightness

    def save(self, pixels: List[RGB]):
        with open(self._file_name, 'w', encoding='utf-8') as file:
            file.write(FORMAT)
            file.write(f'{self._columns} {self._rows}')
            file.write(f'{self._brightness}')
            for pixel in pixels:
                file.write(f'{pixel.r} {pixel.g} {pixel.b}')

