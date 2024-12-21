# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    a, t = map(int, input().split())

    p, q = divmod(a, t)

    if q == 0:
        p -= 1

    print(p)


if __name__ == "__main__":
    main()
