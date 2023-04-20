# -*- coding: utf-8 -*-


def main():
    from math import cos, radians, sqrt
    import sys

    input = sys.stdin.readline

    a, b, h, m = map(int, input().split())
    x = (h * 60 + m) * 360 / 720
    y = m * 360 / 60

    if x < y:
        x, y = y, x
    
    z = x - y
    c = a ** 2 + b ** 2 - 2 * a * b * cos(radians(z))
    print(c ** 0.5)


if __name__ == "__main__":
    main()
