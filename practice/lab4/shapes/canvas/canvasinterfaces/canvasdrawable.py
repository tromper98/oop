from typing import Protocol

from .icanvas import ICanvas


class CanvasDrawable(Protocol):
    def draw(self, canvas: ICanvas):
        ...
