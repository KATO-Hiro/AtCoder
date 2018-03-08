'''input
100 4 16
4554
'''

'''input
20 2 5
84
'''
# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem B


def sum_digit(number):
    string = str(number)
    array = list(map(int, list(string)))
    return sum(array)


if __name__ == '__main__':
    N, A, B = list(map(int, input().split()))

    total = 0

    for number in range(1, N + 1):
        if A <= sum_digit(number) <= B:
            total += number

    print(total)
