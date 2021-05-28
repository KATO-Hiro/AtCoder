# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    t, n = map(int, input().split())
    p, q = divmod(n * 100, t)

    if q != 0:
        p += 1

    print(int(p * (100 + t) / 100) - 1)


if __name__ == "__main__":
    main()
