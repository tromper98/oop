import os
import subprocess
import time
import pytest


from encryptor import *

DATA_DIR = os.path.abspath('data')


def test_crypt_one_string_file():
    file_name = os.path.join(DATA_DIR, 'test2.bin')
    temp_file = os.path.join(DATA_DIR, 'temp.bin')
    temp1_file = os.path.join(DATA_DIR, 'temp1.bin')

    try:
        params = ['python', 'encryptor.py', 'crypt', file_name, temp_file, '255']
        subprocess.run(params, stdout=subprocess.PIPE)

        params = ['python', 'encryptor.py', 'decode', temp_file, temp1_file, '255']
        subprocess.run(params, stdout=subprocess.PIPE)

        with open(temp1_file, 'rb') as f:
            result = f.read()

        with open(file_name, 'rb') as f:
            expected = f.read()

        assert result.split() == expected.split()
    finally:
        os.remove(temp_file)
        os.remove(temp1_file)


def test_crypt_large_file():
    file_name = os.path.join(DATA_DIR, 'test1.bin')
    temp_file = os.path.join(DATA_DIR, 'temp.bin')
    temp1_file = os.path.join(DATA_DIR, 'temp1.bin')

    try:
        params = ['python', 'encryptor.py', 'crypt', file_name, temp_file, '80']
        subprocess.run(params, stdout=subprocess.PIPE)

        params = ['python', 'encryptor.py', 'decode', temp_file, temp1_file, '80']
        subprocess.run(params, stdout=subprocess.PIPE)

        with open(temp1_file, 'rb') as f:
            result = f.read()

        with open(file_name, 'rb') as f:
            expected = f.read()

        assert result.split() == expected.split()
    finally:
        os.remove(temp_file)
        os.remove(temp1_file)


def test_crypt_empty_file():
    file_name = os.path.join(DATA_DIR, 'empty.bin')
    temp_file = os.path.join(DATA_DIR, 'temp.bin')
    temp1_file = os.path.join(DATA_DIR, 'temp1.bin')

    try:
        params = ['python', 'encryptor.py', 'crypt', file_name, temp_file, '120']
        subprocess.run(params, stdout=subprocess.PIPE)

        params = ['python', 'encryptor.py', 'decode', temp_file, temp1_file, '120']
        subprocess.run(params, stdout=subprocess.PIPE)

        with open(temp1_file, 'rb') as f:
            result = f.read()

        with open(file_name, 'rb') as f:
            expected = f.read()

        assert result.split() == expected.split()
    finally:
        os.remove(temp_file)
        os.remove(temp1_file)


def test_crypt_not_found_file():
    file_name = os.path.join(DATA_DIR, 'hot_file.bin')
    params = ['python', 'encryptor.py', 'crypt', file_name, 'data/file.bin', '100']
    res = subprocess.run(params, stdout=subprocess.PIPE)
    assert res.returncode == 1


def test_invalid_key():
    file_name = os.path.join(DATA_DIR, 'test.bin')
    params = ['python', 'encryptor.py', 'crypt', file_name, 'data/file.bin', '290']
    res = subprocess.run(params, stdout=subprocess.PIPE)
    assert res.returncode == 1


def test_crypt_large_picture():
    file_name = os.path.join(DATA_DIR, 'large_picture.jpg')
    params = ['python', 'encryptor.py', 'crypt', file_name, 'data/large_picture-encrypted', '100']
    start_time = time.perf_counter()
    res = subprocess.run(params, stdout=subprocess.PIPE)
    end_time = time.perf_counter()
    assert res.returncode == 0
    print(f'\n Время шифрования файла составило {(end_time - start_time):0.4f} секунд')


def test_shuffle_byte():
    byte = 0b11001110
    expected = 0b01111010
    result = shuffle_bits(byte)
    assert bin(result) == bin(expected)


def test_shuffle_byte_backward():
    byte = 0b01111010
    expected = 0b11001110
    result = shuffle_bits_backward(byte)
    assert bin(result) == bin(expected)
