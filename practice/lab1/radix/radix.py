from typing import List
import sys

ALPHABET = '0123456789ABCDEFHIJKLMNOPQRSTUVWXYZ'


def convert_number(number: str, base_from: int, base_to: int) -> str:
    converted_number = int(number, base_from)
    result = ''
    while converted_number > 0:
        converted_number, digit = divmod(converted_number, base_to)
        result += ALPHABET[digit]
    return result[::-1]


def check_base(base: int):
    if 1 < base < 36:
        return
    raise ValueError(f'Invalid number system. {base} must be in (2, 36) ')


def valid_number_in_base(number: str, base: int) -> None:
    possible_digits = ALPHABET[0: base - 1]
    for digit in number:
        if digit not in possible_digits:
            raise ValueError(f'Invalid number. {number} is not {base}-numeral system')


def parse_params(args: List[str]):
    if len(args) == 4:
        return args[1], int(args[2]), int(args[3])

    if len(args) > 4:
        raise NotImplementedError("Too much parameters was given")

    if len(args) < 4:
        raise NotImplementedError("Not enough parameters was given")


if __name__ == "__main__":
    number, base_from, base_to = parse_params(sys.argv)
    check_base(base_from)
    check_base(base_to)
    valid_number_in_base(number, base_from)
    result = convert_number(number, base_from, base_to)
    print(result, end='\n')
