# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    w, h, x, y = map(int, input().split())
    s = w * h / 2
    flag = 0

    if 2 * x == w and 2 * y == h:
        flag = 1

    print(s, flag)


if __name__ == "__main__":
    main()
