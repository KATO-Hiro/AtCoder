# -*- coding: utf-8 -*-


def main():
    from math import ceil
    import sys
    input = sys.stdin.readline

    n, x, t = map(int, input().split())

    print(ceil(n / x) * t)


if __name__ == '__main__':
    main()
