# -*- coding: utf-8 -*-


def main():
    from math import ceil
    import sys
    input = sys.stdin.readline

    n = int(input())
    odd = ceil(n / 2)
    even = n - odd
    print(3 * odd - 2 * even)


if __name__ == '__main__':
    main()
