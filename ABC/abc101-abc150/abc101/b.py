# -*- coding: utf-8 -*-
# AtCoder Beginner Contest


def sum_digit(number):
    string = str(number)  # 文字列にすることで若干高速化
    array = list(map(int, list(string)))  # list(string)：文字列を1文字のリストに，文字を数値に
    return sum(array)


if __name__ == '__main__':
    n = int(input())
    sn = sum_digit(n)

    if n % sn == 0:
        print('Yes')
    else:
        print('No')
