# -*- coding: utf-8 -*-


def main():
    from math import ceil

    n, d = map(int, input().split())
    print(ceil(n / (2 * d + 1)))


if __name__ == '__main__':
    main()
