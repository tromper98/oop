import os.path
import sys
from typing import Iterator, Iterable
from argparse import ArgumentParser
from bitarray import bitarray

from dataclasses import dataclass

BITE_TRANSPOSE_RULES = [[7, 5], [6, 1], [5, 0], [4, 7], [3, 6], [2, 4], [1, 3], [0, 2]]


@dataclass()
class ProgramArguments:
    def __init__(self, action: str, input_file: str, output_file: str, key: int):
        self.action = action
        self.input_file = input_file
        self.output_file = output_file
        self.key = key


def parse_command_line() -> ProgramArguments:
    parser = ArgumentParser()
    parser.add_argument('action', help='crypt or decrypt data', choices=['crypt', 'decode'], type=str)
    parser.add_argument('input_file', help='file path to file which will crypt/decrypt', type=str)
    parser.add_argument('output_file', help='file path to file where result of crypt/decrypt will be store', type=str)
    parser.add_argument('key', help='number in [0, 255] which used in encryption/decryption algorithm', type=int)

    args = parser.parse_args()
    return ProgramArguments(args.action, args.input_file, args.output_file, args.key)


def file_iterator(input_file: str) -> Iterator[int]:
    input_file = os.path.abspath(input_file)
    with open(input_file, 'rb') as file:
        while chunk := file.read(512): #В двоичном файле уточнить существование строк
            for byte in chunk:
                yield byte


def save_to_file(file_path: str, data_iterator: Iterator[bytes]):
    with open(file_path, 'wb') as file:
        for data in data_iterator:
            file.write(data)


# def xor_byte_and_key(byte: int, key: int) -> bitarray:
#     #Неудачное имя
#     byte_as_bit = bitarray()
#     byte_as_bit.frombytes(byte)
#     key_as_bit = bitarray()
#     key_as_bit.frombytes(key.to_bytes(1, byteorder='little'))
#     return byte_as_bit ^ key_as_bit


#Переделать Обработку байтов
def crypt_byte(byte: int, key: int) -> bytes:
    xor_byte: int = byte ^ key
    crypt_byte = bitarray('00000000')
    for rule in BITE_TRANSPOSE_RULES:
        bit = xor_byte[rule[0]]
        crypt_byte[rule[1]] = bit
    return bytes(crypt_byte)


def decode_byte(byte: bytes, key: int) -> bytes:
    byte_as_bit = bitarray()
    print('byte: ', byte)
    byte_as_bit.frombytes(byte)
    decode_byte = bitarray('00000000')
    for rule in BITE_TRANSPOSE_RULES:
        bit = byte_as_bit[rule[1]]
        decode_byte[rule[0]] = bit
    decode_byte = decode_byte[::-1]
    return bytes(decode_byte ^ key)


def crypt_data(data: Iterable, key: int) -> Iterator[bytes]:
    for byte in data:
        yield crypt_byte(byte, key)


def decode_data(data: Iterable, key: int) -> Iterator[bytes]:
    for byte in data:
        yield decode_byte(byte, key)


def main():
    args: ProgramArguments = parse_command_line()

    if not os.path.isfile(args.input_file):
        print(f'File {args.input_file} doesn\'t exist')
        sys.exit(1)

    if args.key < 0 or args.key > 255:
        print(f'Invalid value key={args.key}. Key must be in [0, 255]')
        sys.exit(1)

    data_iterator = file_iterator(args.input_file)

    if args.action == 'crypt':
        data = crypt_data(data_iterator, args.key)
    else:
        data = decode_data(data_iterator, args.key)

    save_to_file(args.output_file, data)


if __name__ == "__main__":
    main()
