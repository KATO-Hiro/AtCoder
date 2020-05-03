# -*- coding: utf-8 -*-


def main():
    from math import floor
    import sys
    input = sys.stdin.readline

    a, b, n = map(int, input().split())

    if n < b:
        print(floor(a * n / b))
    else:
        x = b - 1
        print(floor(a * x / b) - a * floor(x / b))


if __name__ == '__main__':
    main()
