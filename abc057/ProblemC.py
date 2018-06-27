'''input
1000003
7

9876543210
6

10000
3

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem C


def count_digit(number: int):
    return len(str(number))


if __name__ == '__main__':
    from math import sqrt

    n = int(input())
    result = 11

    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            candidate = max(count_digit(i), count_digit(n // i))
            result = min(result, candidate)

    print(result)
