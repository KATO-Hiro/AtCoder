# -*- coding: utf-8 -*-


def main():
    from math import ceil
    n, a, b, c, d = map(int, input().split())

    print(min(ceil(n / a) * b, ceil(n / c) * d))


if __name__ == '__main__':
    main()
