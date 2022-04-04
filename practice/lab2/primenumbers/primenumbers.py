from argparse import ArgumentParser
from typing import List, Set, Iterable


def parse_upper_bound_from_command_line() -> int:
    parser = ArgumentParser()
    parser.add_argument('upper_bound',
                        help='the upper bound of the set of counting numbers among '
                             'which prime numbers will be searched',
                        type=int)

    args = parser.parse_args()
    return args.upper_bound


def find_prime_numbers(upper_bound: int) -> Set[int]:

    def tag_not_prime_numbers() -> None:
        for i in range(3, int(upper_bound ** 0.5) + 1, 2):
            if sieve[i]:
                sieve[i * i::2 * i] = [False] * ((upper_bound - i * i - 1) // (2 * i) + 1)

    if upper_bound < 2:
        return set()

    upper_bound += 1
    sieve: List[bool] = [True] * upper_bound
    tag_not_prime_numbers()

    prime_numbers: Set[int] = set([2] + [i for i in range(3, upper_bound, 2) if sieve[i]])
    return prime_numbers


def print_array(array: Iterable[int]) -> None:
    print('(', end='')
    for i, number in enumerate(array):
        print(number, end=', ')
        if i % 10 == 0 and i > 0:
            print('')
    print(')')


def main():
    upper_bound = parse_upper_bound_from_command_line()
    prime_numbers: Set[int] = find_prime_numbers(upper_bound)
    print_array(prime_numbers)


if __name__ == '__main__':
    main()
