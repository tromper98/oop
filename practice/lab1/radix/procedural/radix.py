from argparse import ArgumentParser
from dataclasses import dataclass

ALPHABET = '0123456789ABCDEFHIJKLMNOPQRSTUVWXYZ'


@dataclass()
class ProgramArgument:
    def __init__(self, number: str, source_notation: int, target_notation: int):
        self.number: str = number
        self.source_notation: int = source_notation
        self.target_notation: int = target_notation


#Добавить dataclass для аргументов
def parse_command_line() -> ProgramArgument:
    parser = ArgumentParser()

    parser.add_argument('number', help="The number in 'radix_from' to be converted", type=str)
    parser.add_argument('source_notation', help="Radix in which the 'number' is located", type=int)
    parser.add_argument('target_notation', help="Radix in which the 'number' will be converted", type=int)
    args = parser.parse_args()
    return ProgramArgument(args.number, args.source_notation, args.target_notation)


#Неправильный вывод функции
#Лучше назвать checkradix
def validate_annotation(notation: int) -> None:
    if 2 <= notation <= 36:
        return None
    raise ValueError(f'Invalid number system. {notation} must be in [2, 36]')


#radix_from можно сократить до radix
def validate_number(number: str, notation: int) -> None:
    if number[0] == '-':
        number = number[1:]
    possible_digits = ALPHABET[0: notation]
    for digit in number:
        if digit not in possible_digits:
            raise ValueError(f'Invalid number. {number} is not {notation}-numeral system')


#лучше использовать source_radix, target_radix
def convert_number(number: str, source_notation: int, target_notation: int) -> str:

    if number[0] == '-':
        is_negative_number = True
        number: str = number[1:]
    else:
        is_negative_number = False

    converted_number = get_number_from_string(number, source_notation)
    if converted_number == 0:
        return '0'
    #Выделить цикл в отдельную функцию с понятным входом и выходом
    result = convert_notation(converted_number, target_notation)

    if is_negative_number:
        result += '-'

    return result[::-1]


def get_number_from_string(number: str, radix: int) -> int:
    degree = len(number)
    result = 0
    for digit in number:
        degree -= 1
        result = result * radix + int(ALPHABET.index(digit)) #Можно убрать возведение в степень
    return result


def convert_notation(number: int, notation: int) -> str:
    result = ''
    while number > 0:
        number, digit = divmod(number, notation)
        result += ALPHABET[digit]
    return result


#Вместо radix используем notation
#Переименовать функцию в convert_number_annotation
def convert_number_radix_notation() -> None:
    args: ProgramArgument = parse_command_line()
    validate_annotation(args.source_notation)
    validate_annotation(args.target_notation)
    validate_number(args.number, args.source_notation)
    converted_number: str = convert_number(args.number, args.source_notation, args.target_notation)
    print(converted_number)


if __name__ == "__main__":
    convert_number_radix_notation()
