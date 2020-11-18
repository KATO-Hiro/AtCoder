# -*- coding: utf-8 -*-


def main():
    from math import floor
    import sys

    input = sys.stdin.readline

    x, y = map(int, input().split())

    if y == 0:
        print("ERROR")
    else:
        print("{:.2f}".format(floor(x * 100 / y) / 100))


if __name__ == "__main__":
    main()
