# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())

    for _ in range(n):
        hi, mi = map(int, input().split())
        h, m = divmod(mi, 60)
        hi += h
        d, h2 = divmod(hi, 24)
        print(d, h2, m)


if __name__ == "__main__":
    main()
