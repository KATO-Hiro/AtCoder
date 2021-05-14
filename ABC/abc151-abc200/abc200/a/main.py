# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())

    p, q = divmod(n, 100)

    if q >= 1:
        p += 1

    print(p)


if __name__ == "__main__":
    main()
