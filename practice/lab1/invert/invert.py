import os.path
import argparse
from typing import List

from matrix import Matrix


def get_file_path() -> str:
    parser = argparse.ArgumentParser()
    parser.add_argument('file_path', help='Path to the matrix file', type=str)
    args = parser.parse_args()
    return os.path.abspath(args.file_path)


def print_matrix(matrix: List[List[int]]) -> None:
    for row in matrix:
        for number in row:
            print(number, end=' ')
        print()


def calculate_inverse_matrix():
    file_path: str = get_file_path()
    matrix: Matrix = Matrix.from_file(file_path)
    inverse_matrix = matrix.get_inverse_matrix()
    print_matrix(inverse_matrix)


if __name__ == "__main__":
    calculate_inverse_matrix()
