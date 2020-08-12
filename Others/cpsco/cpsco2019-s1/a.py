# -*- coding: utf-8 -*-


def main():
    from math import ceil

    n, a = map(int, input().split())

    print(ceil(a / 3), min(n // 3, a))


if __name__ == '__main__':
    main()
