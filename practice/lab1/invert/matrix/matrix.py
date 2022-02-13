from typing import List

from .impl import MatrixImplementation


class Matrix(MatrixImplementation):
    def __init__(self, matrix: List[List[int]]):
        super().__init__(matrix)

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
            for row in file:
                str_row = row.split(' ')
                matrix.append([int(x) for x in str_row])
        return Matrix(matrix)
