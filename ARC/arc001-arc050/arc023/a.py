# -*- coding: utf-8 -*-


def main():
    from math import floor

    y = int(input())
    m = int(input())
    d = int(input())

    if m == 1 or m == 2:
        y -= 1
        m += 12

    f = (365 * y) + floor(y / 4) - floor(y / 100) + floor(y / 400) + floor(306 * (m + 1) / 10) + d - 429
    print(735369 - f)


if __name__ == '__main__':
    main()
