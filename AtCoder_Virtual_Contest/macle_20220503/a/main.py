# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    p, q = divmod(n, 1000)

    if q == 0:
        print(0)
    else:
        print(1000 - q)


if __name__ == "__main__":
    main()
