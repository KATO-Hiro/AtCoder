# -*- coding: utf-8 -*-

# AtCoder Grand Contest
# Problem A


def sum_digit(number: int):
    return len(str(number))


if __name__ == '__main__':
    number = int(input())

    # See: https://img.atcoder.jp/agc021/editorial.pdf

    sum_max = 0

    while number > 0:
        total_value = sum_digit(number)

        if total_value > sum_max:
            sum_max = total_value
        number -= 1

    print(sum_max)
