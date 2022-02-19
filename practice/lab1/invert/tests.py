import os.path

import pytest

from invert import *

DATA_DIR = os.path.abspath('data')


def test_get_inverse_matrixs():
    files = ['matrix1.txt', 'matrix2.txt', 'matrix3.txt']
    det = -10188
    expected_matrix1 = [
        [4951/det, -3882/det, -1245/det],
        [-2050/det, 1416/det, 462/det],
        [548/det, -414/det, -243/det],
    ]
    det = -1830
    expected_matrix2 = [
        [20/det, 14/det, -30/det],
        [1015/det, -479/det, -150/det],
        [-325/det, 47/det, 30/det],
    ]
    det = -294960
    expected_matrix3 = [
        [-3990/det, 695/det, -4975/det],
        [3156/det, -2250/det, -870/det],
        [-3198/det, -1365/det, 3405/det],
    ]
    expected_matrixs = [expected_matrix1, expected_matrix2, expected_matrix3]
    for i, file in enumerate(files):
        matrix = get_matrix_from_file(os.path.join(DATA_DIR, file))
        determinant = calculate_determinant(matrix)
        inverse_matrix = get_inverse_matrix(matrix, determinant)
        print(inverse_matrix)
        assert [res == exp for res, exp in zip(inverse_matrix, expected_matrixs[i])]


def test_get_empty_file():
    file_name = 'empty_matrix.txt'
    with pytest.raises(SystemExit) as e:
        get_matrix_from_file(os.path.join(DATA_DIR, file_name))
    assert e.type == SystemExit
    assert e.value.code == -1


def test_get_wrong_matrix():
    file_name = 'wrong_matrix.txt'
    with pytest.raises(SystemExit) as e:
        validate_file_path(file_name)
    assert e.type == SystemExit
    assert e.value.code == -1


def test_degenerate_matrix():
    file_name = 'degenerate_matrix.txt'
    with pytest.raises(SystemExit) as e:
        matrix = get_matrix_from_file(os.path.join(DATA_DIR, file_name))
        determinant = calculate_determinant(matrix)
        validate_determinant(determinant)
    assert e.type == SystemExit
    assert e.value.code == -1
