import sys
from dataclasses import dataclass

import argparse

ALPHABET = '0123456789ABCDEFHIJKLMNOPQRSTUVWXYZ'


@dataclass()
class Number:
    def __init__(self, number: str) -> None:
        if number[0] == '-':
            self.is_negative_number = True
            self.number = number[1:]
        else:
            self.is_negative_number = False
            self.number = number

    def __iter__(self) -> str:
        for digit in self.number:
            yield digit

    def __str__(self):
        return '-' + self.number if self.is_negative_number else self.number


class Radix:
    def __init__(self, number: Number, radix_from: int, radix_to: int) -> None:
        self.number: Number = number
        self.radix_from: int = self._check_radix(radix_from)
        self.radix_to: int = self._check_radix(radix_to)
        self._validate_number()

    def convert_number(self) -> Number:
        def _convert_string_to_number(number: str, radix_from: int) -> int:
            degree = 0
            result = 1
            for digit in number:
                result *= int(ALPHABET.index(digit)) * radix_from
                degree += 1
            return result

        converted_number = _convert_string_to_number(self.number.number, self.radix_from)
        if converted_number == 0:
            return Number('0')
        result = ''
        while converted_number > 0:
            converted_number, digit = divmod(converted_number, self.radix_to)
            result += ALPHABET[digit]
        return Number(result[::-1])

    def _check_radix(self, radix: int) -> int:
        if 1 < radix < 36:
            return radix
        raise ValueError(f'Invalid number system. {radix} must be in [2, 36]')

    def _validate_number(self) -> None:
        possible_digits = ALPHABET[0: self.radix_from]
        for digit in self.number:
            if digit not in possible_digits:
                raise ValueError(f'Invalid number. {self.number} is not {self.radix_from}-numeral system')


def parse_params() -> Radix:
    parser = argparse.ArgumentParser()

    parser.add_argument('number', help="The number in 'radix_from' to be converted", type=str)
    parser.add_argument('radix_from', help="Radix in which the 'number' is located", type=int)
    parser.add_argument('radix_to', help="Radix in which the 'number' will be converted", type=int)

    args = parser.parse_args()
    return Radix(Number(args.number), args.radix_from, args.radix_to)


def convert_number():
    radix: Radix = parse_params()
    result: Number = radix.convert_number()
    print(result)
    sys.exit(0)


if __name__ == "__main__":
    convert_number()

