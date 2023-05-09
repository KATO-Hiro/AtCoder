# -*- coding: utf-8 -*-


def main():
    import sys
    from math import atan, degrees, pi, radians

    input = sys.stdin.readline

    a, b, x = map(int, input().split())
    v = a**2 * b

    # See:
    # https://blog.hamayanhamayan.com/entry/2019/10/27/233430
    # △: 水があふれる直前の形状を誤解
    if 2 * x >= v:
        y = (2 * x / (a**2)) - b
        print(degrees(atan((b - y) / a)))
    else:
        y = 2 * x / (a * b)
        print(degrees(atan(b / y)))


if __name__ == "__main__":
    main()
