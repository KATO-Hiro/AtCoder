# -*- coding: utf-8 -*-


def main():
    from math import ceil
    import sys

    input = sys.stdin.readline

    a, b, c, d = map(int, input().split())
    e = d * c - b

    if e <= 0:
        print(-1)
        exit()

    print(ceil(a / e))


if __name__ == "__main__":
    main()
