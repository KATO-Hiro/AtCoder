# -*- coding: utf-8 -*-


def main():
    from math import sqrt
    import sys

    input = sys.stdin.readline

    a, b = map(int, input().split())
    c = 1 / sqrt(a ** 2 + b ** 2)
    print(a * c, b * c)


if __name__ == "__main__":
    main()
