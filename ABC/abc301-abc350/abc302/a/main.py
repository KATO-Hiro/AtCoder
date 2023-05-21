# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    a, b = map(int, input().split())
    p, q = divmod(a, b)

    if q > 0:
        p += 1

    print(p)


if __name__ == "__main__":
    main()
