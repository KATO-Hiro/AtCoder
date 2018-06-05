'''input
15
6

100000
10

'''

# -*- coding: utf-8 -*-

# AtCoder Grand Contest
# Problem A


def sum_digit(number):
    string = str(number)
    array = list(map(int, list(string)))
    return sum(array)


if __name__ == '__main__':
    n = int(input())
    a = 0
    digit_sum_min = 1000000

    for i in range(1, n):
        a = i
        b = n - a

        sum_a = sum_digit(a)
        sum_b = sum_digit(b)
        digit_sum_min = min(digit_sum_min, sum_a + sum_b)

    print(digit_sum_min)
