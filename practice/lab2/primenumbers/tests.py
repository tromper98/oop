import pytest
from primenumbers import *
import math


def find_prime_numbers_slow(upper_bound: int) -> Set[int]:
    def is_prime(number: int) -> bool:
        if number % 2 == 0 and number > 2:
            return False
        for i in range(3, int(math.sqrt(number)) + 1, 2):
            if number % i == 0:
                return False
        return True
    prime_numbers = set()

    if upper_bound < 2:
        return set()

    for i in range(2, upper_bound + 1):
        if is_prime(i):
            prime_numbers.add(i)
    return prime_numbers


def test_find_prime_number_20_upper_bound():
    upper_bound = 20
    res = find_prime_numbers(upper_bound)
    expected = [2, 3, 5, 7, 11, 13, 17, 19]
    assert res == set(expected)


def test_find_prime_number_1000_upper_bound():
    upper_bound = 1000
    res = find_prime_numbers(upper_bound)
    expected: Set[int] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31,
                          37, 41, 43, 47, 53, 59, 61, 67, 71, 73,
                          79, 83, 89, 97, 101, 103, 107, 109, 113,
                          127, 131, 137, 139, 149, 151, 157, 163,
                          167, 173, 179, 181, 191, 193, 197, 199,
                          211, 223, 227, 229, 233, 239, 241, 251,
                          257, 263, 269, 271, 277, 281, 283, 293,
                          307, 311, 313, 317, 331, 337, 347, 349,
                          353, 359, 367, 373, 379, 383, 389, 397,
                          401, 409, 419, 421, 431, 433, 439, 443,
                          449, 457, 461, 463, 467, 479, 487, 491,
                          499, 503, 509, 521, 523, 541, 547, 557,
                          563, 569, 571, 577, 587, 593, 599, 601,
                          607, 613, 617, 619, 631, 641, 643, 647,
                          653, 659, 661, 673, 677, 683, 691, 701,
                          709, 719, 727, 733, 739, 743, 751, 757,
                          761, 769, 773, 787, 797, 809, 811, 821,
                          823, 827, 829, 839, 853, 857, 859, 863,
                          877, 881, 883, 887, 907, 911, 919, 929,
                          937, 941, 947, 953, 967, 971, 977, 983, 991, 997}
    assert res == expected


def test_find_prime_numbers_1_upper_bound():
    upper_bound = 1
    res = find_prime_numbers(upper_bound)
    assert res == set()


def test_count_prime_numbers_100_millions_upper_bound():
    upper_bound = 100000000
    res = find_prime_numbers(upper_bound)
    expected = 5761455
    assert expected == len(res)


def test_prime_numbers_bruteforce():
    upper_bound = 1000
    for i in range(1, upper_bound):
        res = find_prime_numbers(i)
        excepted = find_prime_numbers_slow(i)
        assert res == excepted
