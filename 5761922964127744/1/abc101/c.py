# -*- coding: utf-8 -*-


def main():
    from math import ceil

    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    print(1 + int(ceil((n - k) / (k - 1))))


if __name__ == '__main__':
    main()
