import numpy as np
from typing import List

from complex import Complex
from draw import PPMImage


DEFAULT_RE_POINTS = 500
DEFAULT_IM_POINTS = 500
DEFAULT_MAX_ITERATIONS = 300
DEFAULT_INFINITY_BORDER = 4


class Mandelbrot:
    _re_min: float
    _re_max: float
    _im_min: float
    _im_max: float

    _re_points: int
    _im_points: int
    _max_iterations: int
    _infinity_border: int

    _image: [List[List[int]]]

    def __init__(self, re_min: float, re_max: float, im_min: float, im_max: float):
        self._re_min = re_min
        self._re_max = re_max
        self._im_min = im_min
        self._im_max = im_max

        self._re_points = DEFAULT_RE_POINTS
        self._im_points = DEFAULT_IM_POINTS
        self._max_iterations = DEFAULT_MAX_ITERATIONS
        self._infinity_border = DEFAULT_INFINITY_BORDER
        self._image = []

    def set_figure_size(self, new_re_points: int, new_im_points: int) -> None:
        self._re_points, self._im_points = new_re_points, new_im_points

    def set_max_iterations(self, new_max_iterations) -> None:
        self._max_iterations = new_max_iterations

    def set_infinity_border(self, new_infinity_border):
        self._infinity_border = new_infinity_border

    def calculate_fractal(self):
        self._image.clear()
        new_image: np.ndarray = np.zeros((self._re_points, self._im_points))

        for i_re, re in enumerate(np.linspace(self._re_min, self._re_max, self._re_points)):
            for i_im, im in enumerate(np.linspace(self._im_min, self._im_max, self._im_points)):
                c: Complex = Complex(re, im)

                z: Complex = Complex()
                for iteration in range(self._max_iterations):
                    z = z * z + c

                    if z.magnitude > self._infinity_border:
                        new_image[i_re, i_im] = iteration
                        break

        self._image = -new_image.T

    def save(self, file_name: str, brightness: int):
        saver = PPMImage(file_name, self._re_points, self._im_points, brightness)
        saver.save(self._image)

    @property
    def image(self) -> List[List[int]]:
        return self._image





# def fast_calculate_fractal(self):
#     self._image.clear()
#     image = np.zeros((self._re_points, self._im_points))
#     re, im = np.mgrid[self._re_min:self._re_max:(self._re_points * 1j), self._im_min:self._im_max:(self._im_points * 1j)]
#     c = re + 1j * im
#     z = np.zeros_like(c)
#     for k in range(self._max_iterations):
#         z = z ** 2 + c
#         mask = (np.abs(z) > self._max_iterations) & (image == 0)
#         image[mask] = k
#         z[mask] = np.nan
#
#     self._image = -image.T

