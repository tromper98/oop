from argparse import ArgumentParser
from typing import List, Set


def get_upper_bound() -> int:
    parser = ArgumentParser()
    parser.add_argument('upper_bound',
                        help='the upper bound of the set of counting numbers among '
                             'which prime numbers will be searched',
                        type=int)

    args = parser.parse_args()
    return args.upper_bound


def find_prime_numbers(upper_bound: int) -> List[int]:
    all_numbers: List[bool] = [True] * (upper_bound + 1)
    all_numbers[0] = False
    all_numbers[1] = False

    i = 2
    while i <= upper_bound:
        if all_numbers[i]:
            j = i + i

            while j <= upper_bound:
                all_numbers[j] = False
                j = j + i
        i += 1

    prime_numbers: List[int] = []
    for i, is_prime in enumerate(all_numbers):
        if is_prime:
            prime_numbers.append(i)

    return prime_numbers

