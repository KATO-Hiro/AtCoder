# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split())

    print(x1 ^ x2 ^ x3, y1 ^ y2 ^ y3)


if __name__ == "__main__":
    main()
