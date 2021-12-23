from typing import List


class Matrix:
    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.determinant = self.calculate_determinant()

    def calculate_determinant(self):
        arr = self.matrix
        coeficients: list = [
            arr[0][0] * arr[1][1] * arr[2][2],
            arr[2][0] * arr[0][1] * arr[1][2],
            arr[1][0] * arr[2][1] * arr[0][2],
            -1 * arr[2][0] * arr[1][1] * arr[0][2],
            -1 * arr[0][0] * arr[2][1] * arr[1][2],
            -1 * arr[1][0] * arr[0][1] * arr[2][2]
        ]
        return sum(coeficients)

    def calculate_minors(self) -> List[List[List[List[int]]]]:
        def get_minor(ignore_row: int, ignore_column: int) -> List[List[int]]:
            minor = []
            for i, row in enumerate(self.matrix):
                new_row = []
                if i != ignore_row:
                    for j, number in enumerate(row):
                        if j != ignore_column:
                            new_row.append(number)
                    minor.append(new_row)
            return minor

        minors = []
        for i, row in enumerate(self.matrix):
            minor_row = []
            for j, number in enumerate(row):
                minor_row.append(get_minor(i, j))
            minors.append(minor_row)
        return minors

    def calculate_minors_determinants(self, minors: List[List[List[List[int]]]]) -> List[List[int]]:
        def _get_minor_determinant(minor: List[List[int]]) -> int:
            coefs: list = [
                minor[0][0] * minor[1][1],
                -1 * minor[0][1] * minor[1][0]
            ]
            return sum(coefs)

        determinats = []
        for minor_row in minors:
            determinats_row = []
            for minor in minor_row:
                determinats_row.append(_get_minor_determinant(minor))
            determinats.append(determinats_row)
        return determinats

    def calculate_minor_algebraic_additions_matrix(self, minor_matrix: List[List[int]]) -> List[List[int]]:
        algebraic_additions_matrix = minor_matrix
        algebraic_additions_matrix[0][1] *= -1
        algebraic_additions_matrix[1][2] *= -1
        algebraic_additions_matrix[2][1] *= -1
        algebraic_additions_matrix[1][0] *= -1
        return algebraic_additions_matrix

    def transpose_matrix(self, matrix: List[List[int]]) -> List[List[int]]:
        transpose_matrix = []
        for i in range(len(matrix[0])):
            transpose_matrix.append([x[i] for x in matrix])
        return transpose_matrix

    def inverse_matrix(self) -> List[List[int]]:
        determinant = self.calculate_determinant()
        if not determinant:
            raise ValueError("This matrix doesn't have inverse matrix because determinant = 0")
        minors = self.calculate_minors()
        minors_determinats = self.calculate_minors_determinants(minors)
        minors_determinats = self.calculate_minor_algebraic_additions_matrix(minors_determinats)
        transposed_determinats = self.transpose_matrix(minors_determinats)

        inverse_matrix: List[List[int]] = []
        for transpoded_row in transposed_determinats:
            inverse_matrix.append(list(map(lambda x: x / self.determinant, transpoded_row)))

        return inverse_matrix


class MatrixFactory:
    @staticmethod
    def from_file(filename: str):
        matrix: List[List[int]] = []
        with open(filename, 'r', encoding='utf-8') as file:
            for row in file:
                str_row = row.split(' ')
                matrix.append([int(x) for x in str_row])
        return Matrix(matrix)
