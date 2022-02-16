from typing import List


class Matrix:
    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.determinant = self.calculate_determinant()

    def calculate_determinant(self):
        m = self.matrix
        coefficients: list = [
            m[0][0] * m[1][1] * m[2][2],
            m[2][0] * m[0][1] * m[1][2],
            m[1][0] * m[2][1] * m[0][2],
            -1 * m[2][0] * m[1][1] * m[0][2],
            -1 * m[0][0] * m[2][1] * m[1][2],
            -1 * m[1][0] * m[0][1] * m[2][2]
        ]
        return sum(coefficients)

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
        def get_minor_determinant(minor: List[List[int]]) -> int:
            coefficients: list = [
                minor[0][0] * minor[1][1],
                -1 * minor[0][1] * minor[1][0]
            ]
            return sum(coefficients)

        determinants = []
        for minor_row in minors:
            determinants_row = []
            for minor in minor_row:
                determinants_row.append(get_minor_determinant(minor))
            determinants.append(determinants_row)
        return determinants

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

    def transpose_algebraic_additions_matrix(self, transposed_determinants: List[List[int]]):
        inverse_matrix: List[List[int]] = []
        for transposed_row in transposed_determinants:
            inverse_matrix.append(list(map(lambda x: round(x / self.determinant, 3), transposed_row)))
        return inverse_matrix

    def get_inverse_matrix(self) -> List[List[int]]:
        if not self.determinant:
            raise ValueError("This matrix doesn't have inverse matrix because determinant = 0")
        minors = self.calculate_minors()
        minors_determinants = self.calculate_minors_determinants(minors)
        minors_determinants = self.calculate_minor_algebraic_additions_matrix(minors_determinants)
        transposed_determinants = self.transpose_matrix(minors_determinants)
        inverse_matrix = self.transpose_algebraic_additions_matrix(transposed_determinants)

        return inverse_matrix

    @staticmethod
    def from_file(filename: str):
        matrix: List[List[int]] = []
        with open(filename, 'r', encoding='utf-8') as file:
            for (i, row) in enumerate(file):
                str_row: List[str] = row.split(' ')
                if len(str_row) != 3:
                    raise FileExistsError(f'Size of numbers: {len(str_row)} '
                                          f'in a row does not match the specified size: 3')

                matrix.append([int(x) for x in str_row])
        if len(matrix) != 3:
            raise FileExistsError(f'Number of rows: {len(matrix)} of the matrix '
                                  f'does not match the specified value: 3')
        return Matrix(matrix)
