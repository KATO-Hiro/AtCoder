# -*- coding: utf-8 -*-

# AtCoder Grand Contest
# Problem A

# import math


def sum_digit(number: int):
    string = str(number)
    array = list(map(int, list(string)))
    return sum(array)


if __name__ == '__main__':
    number = int(input())

    sum_max = 0

    while number > 0:
        total_value = sum_digit(number)

        if total_value > sum_max:
            sum_max = total_value
        number -= 1

    print(sum_max)
