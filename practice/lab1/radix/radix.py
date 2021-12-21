from typing import List, Tuple
import sys

ALPHABET = '0123456789ABCDEFHIJKLMNOPQRSTUVWXYZ'


def convert_number(number: str, base_from: int, base_to: int) -> str:
    def _convert_to_10_base(number: str, base_from: int) -> int:
        reversed_number = number[::-1]
        degree = 0
        result = 0
        for digit in reversed_number:
            result += int(ALPHABET.index(digit)) * (base_from ** degree)
            degree += 1
        return result

    converted_number = _convert_to_10_base(number, base_from)
    if converted_number == 0:
        return '0'
    result = ''
    while converted_number > 0:
        converted_number, digit = divmod(converted_number, base_to)
        result += ALPHABET[digit]
    return result[::-1]


def check_base(base: int):
    if 1 < base < 36:
        return
    raise ValueError(f'Invalid number system. {base} must be in (2, 36) ')


def is_negative_number(number: str) -> Tuple[str, bool]:
    is_negative_number: bool = False
    if number[0] == '-':
        is_negative_number = True
        number = number[1:]
    return number, is_negative_number


def valid_number_in_base(number: str, base: int) -> None:
    possible_digits = ALPHABET[0: base]
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
    number, negative_number = is_negative_number(number)
    check_base(base_from)
    check_base(base_to)
    valid_number_in_base(number, base_from)
    result: str = convert_number(number, base_from, base_to)
    result = '-' + result if negative_number else result
    print(result, end='\n')
