from typing import List

from .rgb import RGB
from exceptions.ppmexceptions import *

FORMAT = 'P3'
MAX_COLOR = 'ffffff'


class PPMImage:
    _file_name: str
    _brightness: int

    def __init__(self, file_name: str, brightness: int = 1):
        if not isinstance(file_name, str):
            raise FileNameTypeError(file_name)

        if not 1 <= brightness <= 255:
            raise BrightnessError(brightness)

        self._file_name = file_name
        self._brightness = brightness

    def save(self, pixels: List[List[float]]):
        encoded_pixels = []
        rows = len(pixels)
        columns = len(pixels[0])

        for row in pixels:
            encoded_row = list(map(RGB.from_number, list(map(int, row))))
            encoded_pixels.extend(encoded_row)

        with open(self._file_name, 'w', encoding='utf-8') as file:
            file.write(FORMAT + '\n')
            file.write(f'{rows} {columns}\n')
            file.write(f'{self._brightness}\n')
            for pixel in encoded_pixels:
                file.write(f'{pixel.r} {pixel.g} {pixel.b}\n')
