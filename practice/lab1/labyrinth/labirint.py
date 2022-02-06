import argparse

from . import *


class Labyrinth(LabyrinthImplementation):
    def __init__(self, file_path: str) -> None:
        labyrinth = LabyrinthIO.from_file(file_path)
        super(Labyrinth, self).__init__(labyrinth)

    def find_route_in_labyrinth(self):
        self.calculate_distance()
        self.find_route()


def find_way_in_labyrinth() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file_path', help='Path to the labyrinth file')
    parser.add_argument('output_file_path', help='Path to the file where the found route will be saved')
    args = parser.parse_args()
