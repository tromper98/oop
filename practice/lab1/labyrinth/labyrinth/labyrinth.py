import argparse

from impl import LabyrinthSource, LabyrinthImplementation


class Labyrinth(LabyrinthImplementation):
    def __init__(self, file_path: str) -> None:
        labyrinth = LabyrinthSource.from_file(file_path)
        super(Labyrinth, self).__init__(labyrinth)

    def find_route_in_labyrinth(self):
        self.calculate_distance()
        self.find_route()

    def save_labyrinth_to_file(self, file_path: str):
        LabyrinthSource.save_to_file(self.field, file_path)


def find_way_in_labyrinth() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file_path', help='Path to the labyrinth file')
    parser.add_argument('output_file_path', help='Path to the file where the found route will be saved')
    args = parser.parse_args()

    labyrinth = Labyrinth(args.input_file_path)
    labyrinth.find_route_in_labyrinth()
    labyrinth.save_labyrinth_to_file(args.output_file_path)


if __name__ == "__main__":
    find_way_in_labyrinth()
