from argparse import ArgumentParser, Namespace

ALPHABET = '0123456789ABCDEFHIJKLMNOPQRSTUVWXYZ'


def parse_command_line() -> Namespace:
    parser = ArgumentParser()

    parser.add_argument('number', help="The number in 'radix_from' to be converted", type=str)
    parser.add_argument('radix_from', help="Radix in which the 'number' is located", type=int)
    parser.add_argument('radix_to', help="Radix in which the 'number' will be converted", type=int)

    return parser.parse_args()


def check_radix(radix: int) -> int:
    if 1 < radix < 36:
        return radix
    raise ValueError(f'Invalid number system. {radix} must be in [2, 36]')


def validate_number(number: str, radix_from: int) -> None:
    if number[0] == '-':
        number = number[1:]
    possible_digits = ALPHABET[0: radix_from]
    for digit in number:
        if digit not in possible_digits:
            raise ValueError(f'Invalid number. {number} is not {radix_from}-numeral system')


def convert_number(number: str, radix_from: int, radix_to: int) -> str:
    def _get_number_from_string(number: str, radix_from: int) -> int:
        degree = len(number)
        result = 0
        for digit in number:
            degree -= 1
            result += int(ALPHABET.index(digit)) * radix_from ** degree
        return result

    if number[0] == '-':
        is_negative_number = True
        number: str = number[1:]
    else:
        is_negative_number = False

    converted_number = _get_number_from_string(number, radix_from)
    if converted_number == 0:
        return '0'

    result = ''
    while converted_number > 0:
        converted_number, digit = divmod(converted_number, radix_to)
        result += ALPHABET[digit]

    if is_negative_number:
        result += '-'

    return result[::-1]


def convert_number_radix_from_radix_to() -> None:
    args: Namespace = parse_command_line()
    check_radix(args.radix_from)
    check_radix(args.radix_to)
    validate_number(args.number, args.radix_from)
    converted_number: str = convert_number(args.number, args.radix_from, args.radix_to)
    print(converted_number)


if __name__ == "__main__":
    convert_number_radix_from_radix_to()