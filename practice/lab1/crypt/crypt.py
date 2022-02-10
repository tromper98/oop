from typing import Iterator, Optional, List
from argparse import ArgumentParser, Namespace
from bitarray import bitarray


def parse_params() -> Namespace:
    parser = ArgumentParser()
    parser.add_argument('action', help='crypt or decrypt data', type=str)
    parser.add_argument('input_file', help='file path to file which will crypt/decrypt', type=str)
    parser.add_argument('output_file', help='file path to file where result of crypt/decrypt will be store', type=str)
    parser.add_argument('key', help='number in [0, 255] which used in encryption/decryption algorithm', type=int)

    return parser.parse_args()


def file_read_iterator(file_path: str) -> Iterator[str]:
    try:
        with open(file_path, 'rb', encoding='utf-8') as f:
            yield f.readline()
    except FileNotFoundError:
        raise FileNotFoundError(r"File {file_path} not found")


def file_write_iterator(file_path: str, data: str) -> Iterator[str]:
    with open(file_path, 'rb', encoding='utf-8') as f:
        yield f.write(bytes(data))


def validate_key(key: int):
    if 0 <= key <= 255:
        return
    raise ValueError(f'Invalid value key={key}. Key must be in [0, 255]')


def crypt(row: str, key: int) -> List[int]:
    bytes_row: bytearray = bytearray(row.encode('utf-8'))
    return [byte ^ key for byte in bytes_row]


def encrypt(row: bytearray, key: int) -> List[int]:
    ...


# def shuffle_bits(byte: bytes):
#     shuffle_rules = [[7, 5], [6, 1], [5, 0], [4, 7], [3, 6], [2, 4], [1, 3], [0, 2]]
#     input_bits = bitarray()
#     input_bits.frombytes(byte)
#     output_bits = bitarray('0000 0000')
#     for rule in shuffle_rules:
#         current_rule = shuffle_rules[i]
#         output_bits[] =


a: str = 'abcdefg'
b = crypt(a, 10)
print(list(bytearray(a.encode('utf-8'))))
print(b)


f = 34
bit_f = bitarray()
byte_f = f.to_bytes(1, byteorder='little')
bit_f.frombytes(byte_f)
pass