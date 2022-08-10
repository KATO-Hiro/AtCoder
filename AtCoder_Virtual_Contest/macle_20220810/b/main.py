# -*- coding: utf-8 -*-


def main():
    from math import atan, degrees
    import sys

    input = sys.stdin.readline

    a, b, x = map(int, input().split())
    h = x / (a ** 2)
    y = (2 * a * h) / b  # xが直方体の体積の半分以下
    z = 2 * (b - h)  # xが直方体の体積の半分より大きい

    if ((a ** 2) * b) >= 2 * x:
        print(90 - degrees(atan(y / b)))
    else:
        print(degrees(atan(z / a)))


if __name__ == "__main__":
    main()
