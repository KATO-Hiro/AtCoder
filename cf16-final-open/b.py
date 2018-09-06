# -*- coding: utf-8 -*-


def main():
    from math import ceil
    from math import sqrt

    n = int(input())
    point_min = ceil((-1 + sqrt(1 + 8 * n)) / 2)
    diff = point_min * (point_min + 1) // 2 - n

    for i in range(1, point_min + 1):
        if i != diff:
            print(i)


if __name__ == '__main__':
    main()
