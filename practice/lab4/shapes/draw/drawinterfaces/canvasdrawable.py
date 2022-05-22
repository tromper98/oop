from typing import Protocol

from .canvas import Canvas


class CanvasDrawable(Protocol):
    def draw(self, canvas: Canvas):
        ...
