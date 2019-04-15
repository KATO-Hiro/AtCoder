# -*- coding: utf-8 -*-


def main():
    from math import ceil

    n, t = map(int, input().split())
    a = sum(list(map(int, input().split())))
    print(ceil(a / t))


if __name__ == '__main__':
    main()
