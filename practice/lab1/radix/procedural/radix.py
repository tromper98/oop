from argparse import ArgumentParser
from dataclasses import dataclass

ALPHABET = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'


@dataclass()
class ProgramArguments:
    def __init__(self, number: str, source_notation: int, target_notation: int):
        self.number: str = number
        self.source_notation: int = source_notation
        self.target_notation: int = target_notation


def parse_command_line() -> ProgramArguments:
    parser = ArgumentParser()

    parser.add_argument('number', help="The number in 'radix_from' to be converted", type=str)
    parser.add_argument('source_notation', help="Radix in which the 'number' is located", type=int)
    parser.add_argument('target_notation', help="Radix in which the 'number' will be converted", type=int)
    args = parser.parse_args()
    return ProgramArguments(args.number, args.source_notation, args.target_notation)


def validate_notation(notation: int) -> None:
    if 2 <= notation <= 36:
        return None
    raise ValueError(f'Invalid number system. {notation} must be in [2, 36]')


def validate_number(number: str, notation: int) -> None:
    if number[0] == '-':
        number = number[1:]
    possible_digits = ALPHABET[0: notation]
    for digit in number:
        if digit not in possible_digits:
            raise ValueError(f'Invalid number. {number} is not {notation}-numeral system')


#Перенести обработку - внутрь функцию
def convert_number(number: str, source_notation: int, target_notation: int) -> str:
    converted_number = get_number_from_string(number, source_notation)
    #Перенести внутрь int_to_str
    return int_to_str(converted_number, target_notation)


def get_number_from_string(number: str, notation: int) -> int:
    is_negative_number = False
    if number[0] == '-':
        is_negative_number = True
        number: str = number[1:]

    degree = len(number)
    result = 0
    for digit in number:
        degree -= 1
        result = result * notation + int(ALPHABET.index(digit))

    result = result * -1 if is_negative_number else result
    return result


#Скорее это название int_to_str
def int_to_str(number: int, notation: int) -> str:
    if number == 0:
        return '0'

    is_negative_number = False
    if number < 0:
        is_negative_number = True
        number = abs(number)
    result = ''

    while number > 0:
        number, digit = divmod(number, notation)
        result += ALPHABET[digit]

    if is_negative_number:
        result += '-'
    return result[::-1]


def convert_number_notation() -> None:
    args: ProgramArguments = parse_command_line()
    validate_notation(args.source_notation)
    validate_notation(args.target_notation)
    validate_number(args.number, args.source_notation)
    converted_number: str = convert_number(args.number, args.source_notation, args.target_notation)
    print(converted_number)


if __name__ == "__main__":
    convert_number_notation()
