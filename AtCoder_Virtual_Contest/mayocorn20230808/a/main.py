# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a, b = input().rstrip().split()
    a, b = a[::-1], b[::-1]
    a10, b10 = 0, 0

    for i, ai in enumerate(a):
        a10 += n**i * int(ai)
    for i, bi in enumerate(b):
        b10 += n**i * int(bi)

    print(a10 * b10)


if __name__ == "__main__":
    main()
