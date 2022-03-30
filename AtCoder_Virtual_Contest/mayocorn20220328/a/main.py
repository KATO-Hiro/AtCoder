# -*- coding: utf-8 -*-


def main():
    from math import ceil
    import sys

    input = sys.stdin.readline

    h, a = map(int, input().split())
    print(ceil(h / a))


if __name__ == "__main__":
    main()
