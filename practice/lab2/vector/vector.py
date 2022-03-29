from typing import List


def get_numbers_from_input() -> List[float]:
    numbers: List[str] = input("Enter numbers: ").split()
    return [float(n) for n in numbers]


def process_list(numbers: List[float]) -> None:
    # Multiply each not even number to average value of all even numbers in list
    sum_even: float = 0
    count_even: int = 0
    for number in numbers:
        if number % 2 == 0:
            sum_even += number
            count_even += 1

    if count_even:
        avg = sum_even / count_even
        for i in range(len(numbers)):
            if numbers[i] % 3 == 0:
                numbers[i] *= avg


def print_array(array: List[float]):
    array.sort()
    output: str = ','.join(str(round(n, 3)) for n in array)
    print(output)


def main():
    numbers = get_numbers_from_input()

    process_list(numbers)
    print_array(numbers)


if __name__ == '__main__':
    main()
