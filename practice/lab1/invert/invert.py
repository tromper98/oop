from typing import List


class Matrix:
    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix

    def _is_quadratic_matrix(self) -> bool:
        ln = len(self.matrix)
        for row in self.matrix:
            if len(row) != ln:
                return False
        return True

    def get_determinant(self):
        arr = self.matrix
        coefs: list = [
            arr[0][0] * arr[1][1] * arr[2][2],
            arr[2][0] * arr[0][1] * arr[1][2],
            arr[1][0] * arr[2][1] * arr[0][2],
            -1 * arr[2][0] * arr[1][1] * arr[0][2],
            -1 * arr[0][0] * arr[2][1] * arr[1][2],
            -1 * arr[1][0] * arr[0][1] * arr[2][2]
        ]
        return sum(coefs)

    def get_minors(self) -> List[List[List[List[int]]]]:
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

    def get_minors_determinants(self, minors: List[List[List[List[int]]]]) -> List[List[int]]:
        def get_minor_determinant(minor: List[List[int]]) -> int:
            coefs: list = [
                minor[0][0] * minor[1][1],
                -1 * minor[0][1] * minor[1][0]
            ]
            return sum(coefs)
        determinats = []
        for minor_row in minors:
            determinats_row = []
            for minor in minor_row:
                determinats_row.append(get_minor_determinant(minor))
            determinats.append(determinats_row)
        return determinats

    def get_minor_algebraic_additions_matrix(self, minor_matrix: List[List[int]]) -> List[List[int]]:
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

    def get_inverse_matrix(self) -> List[List[int]]:
        determinant = self.get_determinant()
        if not determinant:
            raise ValueError("This matrix doesn't have inverse matrix because determinant = 0")
        minors = self.get_minors()
        minors_determinats = self.get_minors_determinants(minors)
        minors_determinats = self.get_minor_algebraic_additions_matrix(minors_determinats)
        transposed_determinats = self.transpose_matrix(minors_determinats)
        return transposed_determinats


matrix = [
    [2, 5, 7],
    [6, 3, 4],
    [5, -2, -3]
]

mt = Matrix(matrix)
mt2 = mt.get_inverse_matrix()