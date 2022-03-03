import os.path
import sys
from typing import Iterator, Iterable
from argparse import ArgumentParser
from bitarray import bitarray

from dataclasses import dataclass


@dataclass()
class ProgramArguments:
    def __init__(self, action: str, input_file: str, output_file: str, key: int):
        self.action = action
        self.input_file = input_file
        self.output_file = output_file
        self.key = key


def parse_command_line() -> ProgramArguments:
    parser = ArgumentParser()
    parser.add_argument('action', help='crypt or decrypt data', choices=['crypt', 'encrypt'], type=str)
    parser.add_argument('input_file', help='file path to file which will crypt/decrypt', type=str)
    parser.add_argument('output_file', help='file path to file where result of crypt/decrypt will be store', type=str)
    parser.add_argument('key', help='number in [0, 255] which used in encryption/decryption algorithm', type=int)

    args = parser.parse_args()
    return ProgramArguments(args.action, args.input_file, args.output_file, args.key)


def file_iterator(input_file: str) -> Iterator[bytes]:
    input_file = os.path.abspath(input_file)
    with open(input_file, 'rb') as file:
        for row in file:
            for symbol in row:
                yield symbol.to_bytes(1, byteorder='little')


def save_to_file(file_path: str, data_iterator: Iterator[bytes]):
    with open(file_path, 'wb') as file:
        for data in data_iterator:
            file.write(data)


def xor_byte_with_key(byte: bytes, key: int) -> bitarray:
    byte_as_bit = bitarray()
    byte_as_bit.frombytes(byte)
    key_as_bit = bitarray()
    key_as_bit.frombytes(key.to_bytes(1, byteorder='little'))
    return byte_as_bit ^ key_as_bit


def transpose_bits(source_byte: bitarray, order: str = 'forward') -> bitarray:
    """
    :param source_byte: byte which be transposed
    :param order: swap order. If `forward` - bits will be transpose in transpose_rules
    If 'reverse' - bits will be transpose in reverse order of the rules of the transpose_rules
    """
    if order not in ('forward', 'reverse'):
        raise ValueError(f'Unsupported order method {order}')

    transpose_rules = [[7, 5], [6, 1], [5, 0], [4, 7], [3, 6], [2, 4], [1, 3], [0, 2]]
    source_byte = source_byte[::-1]
    target_byte = bitarray('00000000')
    for rule in transpose_rules:
        if order == 'forward':
            bit = source_byte[rule[0]]
            target_byte[rule[1]] = bit
        else:
            bit = source_byte[rule[1]]
            target_byte[rule[0]] = bit
    return target_byte[::-1]


def crypt_byte(byte: bytes, key: int) -> bytes:
    xor_byte: bitarray = xor_byte_with_key(byte, key)
    return bytes(transpose_bits(xor_byte))


def encrypt_byte(byte: bytes, key: int) -> bytes:
    byte_as_bit = bitarray()
    byte_as_bit.frombytes(byte)
    transpose_byte = bytes(transpose_bits(byte_as_bit, order='reverse'))
    return bytes(xor_byte_with_key(transpose_byte, key))


def crypt_data(data: Iterable, key: int) -> Iterator[bytes]:
    for byte in data:
        yield crypt_byte(byte, key)


def encrypt_data(data: Iterable, key: int) -> Iterator[bytes]:
    for byte in data:
        yield encrypt_byte(byte, key)


def main():
    args: ProgramArguments = parse_command_line()

    if not os.path.isfile(args.input_file):
        print(f'File {args.input_file} doesn\'t exists')
        sys.exit(1)

    if args.key < 0 or args.key > 255:
        print(f'Invalid value key={args.key}. Key must be in [0, 255]')
        sys.exit(1)

    data_iterator = file_iterator(args.input_file)

    if args.action == 'crypt':
        data = crypt_data(data_iterator, args.key)
    else:
        data = encrypt_data(data_iterator, args.key)
    save_to_file(args.output_file, data)
    sys.exit(0)


if __name__ == "__main__":
    main()
