# -*- coding: utf-8 -*-
# AtCoder Beginner Contest


def main():
    from math import pi

    n = int(input())
    r = sorted([int(input()) for _ in range(n)], reverse=True)
    summed_r = 0

    for index, ri in enumerate(r):
        if index % 2 == 0:
            summed_r += ri ** 2
        else:
            summed_r -= ri ** 2

    print(summed_r * pi)


if __name__ == '__main__':
    main()
