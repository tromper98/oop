from typing import List, Callable


def get_list_from_args() -> List[float]:
    numbers: list = input("Enter numbers: ").split()
    return [round(float(n), 3) for n in numbers]


def add_avg_for_each_number(numbers: List[float]) -> List[float]:
    avg: float = sum(numbers) / len(numbers)
    return [round(n * avg, 3) if n > 0 else n for n in numbers]


def multiply_numbers_by_min(numbers: List[float]) -> List[float]:
    min_number: float = min(numbers)
    return [round(n * min_number, 3) for n in numbers]


def multiply_numbers_mod_3_zero(numbers: List[float]) -> List[float]:
    even_numbers: List[float] = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)

    if not even_numbers:
        return []

    avg_even_numbers: float = sum(even_numbers) / len(even_numbers)
    return [round(n * avg_even_numbers, 3) if n % 3 == 0 else n for n in numbers]


def divide_numbers_by_half_max(numbers: List[float]) -> List[float]:
    half_max: float = max(numbers) / 2
    return [round(n / half_max, 3) for n in numbers]


def multiply_negative_max_and_min(numbers: List[float]) -> List[float]:
    max_num: float = max(numbers)
    min_num: float = min(numbers)
    return [round(n * max_num * min_num, 3) if n < 0 else n for n in numbers]


def multiply_numbers_max_and_divide_min(numbers: List[float]) -> List[float]:
    max_num: float = max(numbers)
    min_num: float = min(numbers)
    return [round(n * max_num / min_num, 3) for n in numbers]


def print_function_result(description: str, func: Callable, numbers: List[float]) -> None:
    print('-' * 5, description, '-' * 5, sep='', end='\n\n')
    result = func(numbers)
    print(result, end='\n\n')
    print('-' * (len(description) + 10), end='\n\n')


if __name__ == '__main__':
    numbers = get_list_from_args()

    print_function_result('add avg for each number',
                          add_avg_for_each_number,
                          numbers)

    print_function_result('multiple each number by min',
                          multiply_numbers_by_min,
                          numbers)

    print_function_result('multiply numbers mod 3 zero',
                          multiply_numbers_mod_3_zero,
                          numbers)

    print_function_result('divide numbers by half max',
                          divide_numbers_by_half_max,
                          numbers)

    print_function_result('multiply negative max and min',
                          multiply_negative_max_and_min,
                          numbers)

    print_function_result('multiply numbers max and divide min',
                          multiply_numbers_max_and_divide_min,
                          numbers)
