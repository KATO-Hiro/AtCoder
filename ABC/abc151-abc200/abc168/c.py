# -*- coding: utf-8 -*-


def main():
    from math import cos
    import sys
    input = sys.stdin.readline

    a, b, h, m = map(int, input().split())
    c = (a ** 2) + (b ** 2) - 2 * a * b * cos((5 * h - m) * 6)
    print(c ** 0.5)
    print(360 - ((5 * h - m) * 6))


if __name__ == '__main__':
    main()
