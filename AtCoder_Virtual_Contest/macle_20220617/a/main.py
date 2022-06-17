# -*- coding: utf-8 -*-


def main():
    from math import ceil
    import sys

    input = sys.stdin.readline

    n = int(input())
    print(ceil(n / 100))


if __name__ == "__main__":
    main()
