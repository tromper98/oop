from argparse import ArgumentParser
from typing import List, Set
import math

def parse_upper_bound_from_command_line() -> int:
    parser = ArgumentParser()
    parser.add_argument('upper_bound',
                        help='the upper bound of the set of counting numbers among '
                             'which prime numbers will be searched',
                        type=int)

    args = parser.parse_args()
    return args.upper_bound


def is_prime(number: int) -> bool:
    if number % 2 == 0 and number > 2:
        return False
    for i in range(3, int(math.sqrt(number)) + 1, 2):
        if number % i == 0:
            return False
    return True

#Убрать Optional
def find_prime_numbers(upper_bound: int) -> Set[int]:

    def tag_not_prime_numbers() -> None:
        for i in range(3, int(upper_bound ** 0.5) + 1, 2):
            if sieve[i]:
                sieve[i * i::2 * i] = [False] * ((upper_bound - i * i - 1) // (2 * i) + 1)

    if upper_bound < 2:
        return set()
    sieve: List[bool] = [True] * upper_bound
    tag_not_prime_numbers()

    prime_numbers: Set[int] = set([2] + [i for i in range(3, upper_bound, 2) if sieve[i]])
    if is_prime(upper_bound):
        prime_numbers.add(upper_bound)
    return prime_numbers


def main():
    upper_bound = parse_upper_bound_from_command_line()
#Правильно выводить пустой список, когда < 2
#Не выводится последнее простое число, если оно равно upper_bound
#При upper_bound = 15 падает тест
    prime_numbers: Set[int] = find_prime_numbers(upper_bound)
    print(prime_numbers)


if __name__ == '__main__':
    main()
