import os.path
import sys
from typing import Iterator, Iterable
from argparse import ArgumentParser

from dataclasses import dataclass

# 7 >> 2: 5
# 6 >> 5: 1
# 5 >> 5: 0
# 4 << 3: 7
# 3 << 3: 6
# 2 << 2: 4
# 1 << 2: 3
# 0 << 2: 2


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


def shuffle_bits(byte: int) -> int:
    result: int = 0
    result += (byte << 2 & 0b00011100)
    result += (byte << 3 & 0b11000000)
    result += (byte >> 5 & 0b00000011)
    result += (byte >> 2 & 0b00100000)
    return result


def shuffle_bits_backward(byte: int) -> int:
    result: int = 0
    result += (byte >> 2 & 0b00000111)
    result += (byte >> 3 & 0b00011000)
    result += (byte << 5 & 0b01100000)
    result += (byte << 2 & 0b10000000)
    return result


def file_iterator(input_file: str) -> Iterator[int]:
    input_file = os.path.abspath(input_file)
    with open(input_file, 'rb') as file:
        while chunk := file.read(512):
            for byte in chunk:
                yield byte


def save_to_file(file_path: str, data_iterator: Iterator[int]):
    with open(file_path, 'wb') as file:
        for number in data_iterator:
            file.write(number.to_bytes(length=1, byteorder='little'))


def crypt_number(number: int, key: int) -> int:
    xor_byte: int = number ^ key
    return shuffle_bits(xor_byte)


def decode_number(number: int, key: int) -> int:
    shuffled_number = shuffle_bits_backward(number)
    return shuffled_number ^ key


def crypt_data(data: Iterable, key: int) -> Iterator[int]:
    for number in data:
        yield crypt_number(number, key)


def decode_data(data: Iterable, key: int) -> Iterator[int]:
    for byte in data:
        yield decode_number(byte, key)


def main() -> None:
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
