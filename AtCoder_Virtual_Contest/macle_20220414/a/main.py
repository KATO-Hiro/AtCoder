# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    a, b = map(int, input().split())
    c, d = map(int, input().split())

    print(a * d - b * c)


if __name__ == "__main__":
    main()
