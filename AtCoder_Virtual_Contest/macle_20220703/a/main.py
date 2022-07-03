# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    a, b, c, k = map(int, input().split())

    if k % 2 == 0:
        print(a - b)
    else:
        print(b - a)


if __name__ == "__main__":
    main()
