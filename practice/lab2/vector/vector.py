import sys
from typing import List, Callable, Optional


def get_numbers_from_input() -> List[float]:
    numbers: list = input("Enter numbers: ").split()
    return [round(float(n), 3) for n in numbers]


def calculate_result(numbers: List[float]) -> List[float]:
    # Multiply each not even number to average value of all even numbers
    even_numbers: List[float] = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)

    if even_numbers:
        avg: float = sum(even_numbers) / len(even_numbers)
        for i in range(len(numbers)):
            if numbers[i] % 3 == 0:
                numbers[i] *= avg
    return numbers


def print_array(array: List[float]):
    output: str = ','.join(str(n) for n in array)
    print(output)


def main():
    numbers = get_numbers_from_input()
    if len(numbers) == 0:
        print('List is empty')
        sys.exit(1)

    result: List[float] = calculate_result(numbers)
    print_array(result)


if __name__ == '__main__':
    main()
