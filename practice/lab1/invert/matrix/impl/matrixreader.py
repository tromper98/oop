from typing import List


class MatrixReader:
    @staticmethod
    def from_file(filename: str):
        matrix: List[List[int]] = []
        with open(filename, 'r', encoding='utf-8') as file:
            for row in file:
                str_row = row.split(' ')
                matrix.append([int(x) for x in str_row])
        return matrix
