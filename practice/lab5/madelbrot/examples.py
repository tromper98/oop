import pytest

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation, rc

from mandelbrot import Mandelbrot


def mandelbrot_example():
    mandelbrot = Mandelbrot(-2.5, 1.5, -2.5, 2.5)
    mandelbrot.set_figure_size(1500, 1500)
    mandelbrot.set_max_iterations(300)
    mandelbrot.set_infinity_border(4)
    mandelbrot.calculate_fractal()
    mandelbrot.save('./test4.ppm', 180)

    plt.xticks([])
    plt.yticks([])
    plt.imshow(mandelbrot.image, cmap='flag', interpolation='none')


def animate_mandelbrot_example():
    rc('animation', html='html5')

    figure = plt.figure(figsize=(10, 10))
    max_frames = 200
    max_zoom = 300

    re_min = -2.5
    re_max = 1.5
    im_min = -2
    im_max = 2

    images = []

    def init():
        return plt.gca()

    def animate(i):
        if i > max_frames // 2:

            plt.imshow(images[max_frames // 2 - i], cmap='flag')
            return

        re_center, im_center = -0.793191078177363, 0.16093721735804
        zoom = (i / max_frames * 2) ** 3 * max_zoom + 1
        scale_factor = 1 / zoom
        new_re_min = (re_min - re_center) * scale_factor + re_center
        new_im_min = (im_min - im_center) * scale_factor + im_center
        new_re_max = (re_max - re_center) * scale_factor + re_center
        new_im_max = (im_max - im_center) * scale_factor + im_center
        mandelbrot = Mandelbrot(new_re_min, new_re_max, new_im_min, new_im_max)
        mandelbrot.set_figure_size(1000, 1000)

        mandelbrot.calculate_fractal()

        plt.imshow(mandelbrot.image, cmap='flag')
        images.append(mandelbrot.image)

        return plt.gca()

    anim = animation.FuncAnimation(figure, animate, init_func=init, frames=max_frames, interval=50)
    writer = animation.PillowWriter(fps=30)
    file_name = './animation1.gif'
    anim.save(file_name, writer)


animate_mandelbrot_example()

