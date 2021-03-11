# -*- coding: utf-8 -*-


def f(a, b, c, t):
    from math import sin, pi

    return a * t + b * sin(c * t * pi)


def main():
    import sys

    input = sys.stdin.readline

    a, b, c = map(int, input().split())
    low = 0
    high = 200

    for i in range(100):
        mid = (low + high) / 2
        result = f(a, b, c, mid)

        if result < 100:
            low = mid
        else:
            high = mid

    print(low)


if __name__ == "__main__":
    main()
