import sys
import os.path
import argparse
from typing import List


def file_path_from_command_line() -> str:
    parser = argparse.ArgumentParser()
    parser.add_argument('file_path', help='Path to the matrix file', type=str)
    args = parser.parse_args()
    return os.path.abspath(args.file_path)


def validate_file_path(file_path: str) -> None:
    file_path = os.path.abspath(file_path)
    if os.path.isfile(file_path):
        return
    print(f'File {file_path} doesn\'t exists')
    sys.exit(-1)


def validate_3x3_matrix(matrix: List[List[float]]):
    if len(matrix) != 3:
        print('The number of rows of the matrix is not equal to 3')
        sys.exit('-1')

    for row in matrix:
        if len(row) != 3:
            print(f'Row contains {len(row)} numbers although must be 3 numbers')
            sys.exit('-1')


def validate_determinant(determinant: float):
    if determinant:
        return
    # Это исключение стоит перехватить в функции main
    print("This matrix doesn't have inverse matrix because determinant = 0")
    sys.exit(-1)


def get_matrix_from_file(file_path: str):
    file_path = os.path.abspath(file_path)

    if os.stat(file_path).st_size == 0:
        print(f'File {file_path} is empty')
        sys.exit(-1)

    matrix: List[List[float]] = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for (i, row) in enumerate(file):
            str_row: List[str] = row.split(' ')
            matrix.append([float(x) for x in str_row])
    return matrix


def calculate_determinant(matrix: List[List[float]]) -> float:
    m = matrix
    # Список лишний. Можно заменить сложением
    determinant = m[0][0] * m[1][1] * m[2][2] + \
                  m[2][0] * m[0][1] * m[1][2] + \
                  m[1][0] * m[2][1] * m[0][2] + \
                  -1 * m[2][0] * m[1][1] * m[0][2] + \
                  -1 * m[0][0] * m[2][1] * m[1][2] + \
                  -1 * m[1][0] * m[0][1] * m[2][2]
    return determinant


# Лучше объединить с предыдущим методом
def calculate_minors_determinants(matrix: List[List[float]]) -> List[List[float]]:
    def _get_minor(ignore_row: int, ignore_column: float) -> List[List[float]]:
        minor = []
        for i, row in enumerate(matrix):
            new_row = []
            if i != ignore_row:
                for j, number in enumerate(row):
                    if j != ignore_column:
                        new_row.append(number)
                minor.append(new_row)
        return minor

    # Лучше назвать get_2x2_determinant
    def _get_2x2_determinant(matrix: List[List[float]]) -> float:
        return matrix[0][0] * matrix[1][1] + -1 * matrix[0][1] * matrix[1][0]

    minor_determinants: List[List[float]] = []
    for i, row in enumerate(matrix):
        minor_determinants_row: List[float] = []
        for j, number in enumerate(row):
            minor = _get_minor(i, j)
            minor_determinants_row.append(_get_2x2_determinant(minor))
        minor_determinants.append(minor_determinants_row)
    return minor_determinants


def get_algebraic_additions_matrix(matrix: List[List[float]]) -> List[List[float]]:
    algebraic_additions_matrix = matrix
    algebraic_additions_matrix[0][1] *= -1
    algebraic_additions_matrix[1][2] *= -1
    algebraic_additions_matrix[2][1] *= -1
    algebraic_additions_matrix[1][0] *= -1
    return algebraic_additions_matrix


def transpose_matrix(matrix: List[List[float]]) -> List[List[float]]:
    transposed_matrix: List[List[float]] = []
    for i in range(len(matrix[0])):
        transposed_matrix.append([x[i] for x in matrix])
    return transposed_matrix


def divide_matrix_by_determinant(matrix: List[List[float]], determinant: float):
    inverse_matrix: List[List[float]] = []
    for row in matrix:
        inverse_matrix.append(list(map(lambda x: x / determinant, row)))
    return inverse_matrix


def get_inverse_matrix(matrix: List[List[float]], determinant: float) -> List[List[float]]:
    minors_determinants = calculate_minors_determinants(matrix)
    algebraic_addition_matrix = get_algebraic_additions_matrix(minors_determinants)
    transposed_matrix = transpose_matrix(algebraic_addition_matrix)
    inverse_matrix = divide_matrix_by_determinant(transposed_matrix, determinant)

    return inverse_matrix


def print_matrix(matrix: List[List[float]]) -> None:
    for row in matrix:
        for number in row:
            print(number, end=' ')
        print()


def calculate_inverse_matrix():
    file_path: str = file_path_from_command_line()
    validate_file_path(file_path)

    matrix: List[List[float]] = get_matrix_from_file(file_path)
    validate_3x3_matrix(matrix)

    determinant: float = calculate_determinant(matrix)
    validate_determinant(determinant)

    inverse_matrix: List[List[float]] = get_inverse_matrix(matrix, determinant)
    print_matrix(inverse_matrix)


if __name__ == "__main__":
    calculate_inverse_matrix()
