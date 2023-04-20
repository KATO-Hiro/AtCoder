# -*- coding: utf-8 -*-


def law_of_cosines(a, b, theta_degree):
    from math import cos, radians, sqrt

    c = a ** 2 + b ** 2 - 2 * a * b * cos(radians(theta_degree))
    return sqrt(c)


def main():
    import sys

    input = sys.stdin.readline

    a, b, h, m = map(int, input().split())
    x = (h * 60 + m) * 360 / 720
    y = m * 360 / 60
    print(law_of_cosines(a, b, abs(x - y)))


if __name__ == "__main__":
    main()
