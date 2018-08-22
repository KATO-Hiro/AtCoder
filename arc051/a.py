# -*- coding: utf-8 -*-


def main():
    from math import sqrt

    x1, y1, r = list(map(int, input().split()))
    x2, y2, x3, y3 = list(map(int, input().split()))

    if (x2 <= x1 - r) and (x1 + r <= x3) and (y2 <= y1 - r) and (y1 + r <= y3):
        print('NO')
    else:
        print('YES')

    x = r ** 2 - (y1 - y2) ** 2
    y = r ** 2 - (x1 - x2) ** 2

    if x < 0 or y < 0:
        print('YES')
        exit()

    sqrt_x = sqrt(x)
    sqrt_y = sqrt(y)

    if (x1 - sqrt_x <= x2) and (x3 <= x1 + sqrt_x) and (y1 - sqrt_y <= y2) and (y3 <= y1 + sqrt_y):
        print('NO')
    else:
        print('YES')


if __name__ == '__main__':
    main()
