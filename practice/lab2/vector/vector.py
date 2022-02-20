import sys
from typing import List, Callable


def get_numbers_from_input() -> List[float]:
    numbers: list = input("Enter numbers: ").split()
    return [round(float(n), 3) for n in numbers]


def multiply_numbers_mod_3_zero_to_even_avg(numbers: List[float]) -> List[float]:
    even_numbers: List[float] = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)

    if not even_numbers:
        return []

    avg_even_numbers: float = sum(even_numbers) / len(even_numbers)
    return [round(n * avg_even_numbers, 3) if n % 3 == 0 else n for n in numbers]


def print_function_result(description: str, func: Callable, numbers: List[float]) -> None:
    print('-' * 5, description, '-' * 5, sep='', end='\n\n')
    result = func(numbers)
    print(result.sort(), end='\n\n')
    print('-' * (len(description) + 10), end='\n\n')


if __name__ == '__main__':
    numbers = get_numbers_from_input()

    if len(numbers) == 0:
        print('List is empty')
        sys.exit(1)

    print_function_result('multiply numbers mod 3 zero',
                          multiply_numbers_mod_3_zero_to_even_avg,
                          numbers)
