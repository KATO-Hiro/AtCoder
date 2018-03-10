'''input
6
382253568 723152896 37802240 379425024 404894720 471526144
4
5 6 8 10
3
8 12 40
'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem B


def count_operation(numbers):
    is_even = True
    count = 0

    while is_even is True:
        elements = divided_by(2 ** (count + 1), numbers)

        if elements.count(0) == number_count:
            count += 1
        else:
            is_even = False
    return count


def divided_by(number, numbers):
    return [element % number for element in numbers]


if __name__ == '__main__':
    number_count = int(input())
    numbers = list(map(int, input().split()))

    result = count_operation(numbers)
    print(result)
