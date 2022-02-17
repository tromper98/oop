from argparse import ArgumentParser
from labyrinthclass import Labyrinth


class ProgramArguments:
    def __init__(self, input_file: str, output_file: str):
        self.input_file = input_file
        self.output_file = output_file


def parse_command_line():
    parser = ArgumentParser()
    parser.add_argument('input_file_path', help='Path to the labyrinth file')
    parser.add_argument('output_file_path', help='Path to the file where the found route will be saved')
    args = parser.parse_args()
    return ProgramArguments(args.input_file_path, args.output_file_path)


def find_way_in_labyrinth() -> None:
    args: ProgramArguments = parse_command_line()
    labyrinth = Labyrinth.from_file(args.input_file)
    labyrinth.find_route_in_labyrinth()
    labyrinth.save_labyrinth_to_file(args.output_file)


if __name__ == "__main__":
    find_way_in_labyrinth()
