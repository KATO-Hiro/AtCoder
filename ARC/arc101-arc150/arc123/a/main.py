# -*- coding: utf-8 -*-


def main():
    from math import ceil
    import sys

    input = sys.stdin.readline

    a1, a2, a3 = map(int, input().split())
    x = 2 * a2 - a1 - a3
    k0 = max(0, ceil(-x / 2))

    print(x + 3 * k0)


if __name__ == "__main__":
    main()
