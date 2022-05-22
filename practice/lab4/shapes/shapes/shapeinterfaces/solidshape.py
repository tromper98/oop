from shapes.shapeinterfaces.shape import Shape


class SolidShape(Shape):
    def get_fill_color(self) -> int:
        ...
