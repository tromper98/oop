import os.path
from typing import Iterator, Iterable, Optional, List
from argparse import ArgumentParser
from bitarray import bitarray

from dataclasses import dataclass


@dataclass()
class ProgramArgument:
    def __init__(self, action: str, input_file: str, output_file: str, key: int):
        self.action = action
        self.input_file = input_file
        self.output_file = output_file
        self.key = key


def parse_params() -> ProgramArgument:
    parser = ArgumentParser()
    parser.add_argument('action', help='crypt or decrypt data', type=str)
    parser.add_argument('input_file', help='file path to file which will crypt/decrypt', type=str)
    parser.add_argument('output_file', help='file path to file where result of crypt/decrypt will be store', type=str)
    parser.add_argument('key', help='number in [0, 255] which used in encryption/decryption algorithm', type=int)

    args = parser.parse_args()
    return ProgramArgument(args.action, args.input_file, args.output_file, args.key)


def validate_action(action: str) -> None:
    if action in ['crypt', 'encrypt']:
        return
    raise ValueError(f"Invalid {action}. Action may by 'crypt' or 'encrypt'")


def check_file_exists(file_path: str) -> None:
    file_path = os.path.abspath(file_path)
    if os.path.isfile(file_path):
        return
    raise FileNotFoundError(f'File {file_path} doesn\'t exists')


def file_iterator(input_file: str) -> Iterator[bytes]:
    input_file = os.path.abspath(input_file)
    with open(input_file, 'rb') as file:
        for row in file:
            for symbol in row:
                yield symbol.to_bytes(1, byteorder='little')


def save_to_file(file_name: str, data_iterator: Iterator[bytes]):
    output_file: str = os.path.abspath(file_name)
    with open(output_file, 'wb') as file:
        for data in data_iterator:
            file.write(data)


def validate_key(key: int):
    if 0 <= key <= 255:
        return
    raise ValueError(f'Invalid value key={key}. Key must be in [0, 255]')


def validate_params(args: ProgramArgument):
    validate_action(args.action)
    validate_key(args.key)
    check_file_exists(args.input_file)


def encrypt(row: bytearray, key: int) -> List[int]:
    ...


def xor_byte_with_key(byte: bytes, key: int) -> bitarray:
    byte_as_bit = bitarray()
    byte_as_bit.frombytes(byte)
    key_as_bit = bitarray()
    key_as_bit.frombytes(key.to_bytes(1, byteorder='little'))
    return byte_as_bit ^ key_as_bit


def transpose_bits(source_byte: bitarray) -> bitarray:
    transpose_rules = [[7, 5], [6, 1], [5, 0], [4, 7], [3, 6], [2, 4], [1, 3], [0, 2]]
    source_byte = source_byte[::-1]
    target_byte = bitarray('00000000')
    for rule in transpose_rules:
        bit = source_byte[rule[0]]
        target_byte[rule[1]] = bit
    return target_byte[::-1]


def crypt_byte(byte: bytes, key: int) -> bytes:
    xor_byte: bitarray = xor_byte_with_key(byte, key)
    return bytes(transpose_bits(xor_byte))


def crypt_data(input_data: Iterable, key: int) -> Iterator[bytes]:
    for byte in input_data:
        yield crypt_byte(byte, key)


def main():
    args: ProgramArgument = parse_params()
    validate_params(args)
    if args.action == 'crypt':
        data_iterator = file_iterator(args.input_file)
        data = crypt_data(data_iterator, args.key)
        save_to_file(args.output_file, data)


if __name__ == "__main__":
    main()
