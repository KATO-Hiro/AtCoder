# -*- coding: utf-8 -*-


def main():
    from math import ceil
    n, k = map(int, input().split())

    if ceil(n / 2) < k:
        print('NO')
    else:
        print('YES')


if __name__ == '__main__':
    main()
