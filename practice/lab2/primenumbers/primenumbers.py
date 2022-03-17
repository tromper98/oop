import sys
from argparse import ArgumentParser
from typing import List, Optional


def get_upper_bound() -> int:
    parser = ArgumentParser()
    parser.add_argument('upper_bound',
                        help='the upper bound of the set of counting numbers among '
                             'which prime numbers will be searched',
                        type=int)

    args = parser.parse_args()
    return args.upper_bound


def find_prime_numbers(upper_bound: int) -> Optional[List[int]]:
    if upper_bound == 1:
        return []

    sieve: List[bool] = [True] * (upper_bound + 1)

    for i in range(3, int(upper_bound ** 0.5) + 1, 2):
        if sieve[i]:
            sieve[i*i::2*i] = [False]*((upper_bound-i*i-1)//(2*i)+1)

    return [2] + [i for i in range(3, upper_bound, 2) if sieve[i]]


def main():
    upper_bound = get_upper_bound()

    if upper_bound < 2:
        print('upper_bound must be integer >= 2')
        sys.exit(1)

    prime_numbers: List[int] = find_prime_numbers(upper_bound)
    for number in prime_numbers:
        print(number)


if __name__ == '__main__':
    main()
