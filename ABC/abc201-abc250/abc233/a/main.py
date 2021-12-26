# -*- coding: utf-8 -*-


def main():
    from math import ceil
    import sys

    input = sys.stdin.readline

    x, y = map(int, input().split())

    if y - x <= 0:
        print(0)
    else:
        y -= x
        print(ceil(y / 10))


if __name__ == "__main__":
    main()
