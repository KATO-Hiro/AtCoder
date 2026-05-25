# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s, p, r = map(int, input().split())
    m = int(input())

    for _ in range(m):
        ei, vi = map(int, input().split())

        if ei == 1:
            s += vi
        else:
            s -= vi * p

    print(s - r)


if __name__ == "__main__":
    main()
