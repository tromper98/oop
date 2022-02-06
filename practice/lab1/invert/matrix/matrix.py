from typing import List

from matrix.impl import MatrixImplementation
from matrix.factory import MatrixIO


class Matrix(MatrixImplementation):
    def __init__(self, file_path: str):
        matrix = MatrixIO.from_file(file_path)
        super().__init__(matrix)

    def get_inverse_matrix(self) -> List[List[int]]:
        determinant = self.calculate_determinant()
        if not determinant:
            raise ValueError("This matrix doesn't have inverse matrix because determinant = 0")
        minors = self.calculate_minors()
        minors_determinants = self.calculate_minors_determinants(minors)
        minors_determinants = self.calculate_minor_algebraic_additions_matrix(minors_determinants)
        transposed_determinants = self.transpose_matrix(minors_determinants)

        inverse_matrix: List[List[int]] = []
        for transposed_row in transposed_determinants:
            inverse_matrix.append(list(map(lambda x: x / self.determinant, transposed_row)))

        return inverse_matrix