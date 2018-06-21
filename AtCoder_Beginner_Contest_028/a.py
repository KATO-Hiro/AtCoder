# -*- coding: utf-8 -*-
# AtCoder Beginner Contest


if __name__ == '__main__':
    n = int(input())

    if n == 100:
        print('Perfect')
    elif 90 <= n <= 99:
        print('Great')
    elif 60 <= n <= 89:
        print('Good')
    else:
        print('Bad')
