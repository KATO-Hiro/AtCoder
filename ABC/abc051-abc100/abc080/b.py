'''input
57
12
'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem B


def is_harshad_number(number):
    if number % sum_digit(number) == 0:
        return "Yes"
    else:
        return "No"


def sum_digit(number):
    return sum(list(map(int, list(str(number)))))


if __name__ == '__main__':
    number = int(input())

    result = is_harshad_number(number)
    print(result)
