# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    a, b = map(int, input().split())
    c = 1 / (a ** 2 + b ** 2) ** 0.5
    print(a * c, b * c)


if __name__ == "__main__":
    main()
