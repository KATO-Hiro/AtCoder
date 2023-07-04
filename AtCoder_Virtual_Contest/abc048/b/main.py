# -*- coding: utf-8 -*-


def f(n, x):
    return n // x


def main():
    import sys

    input = sys.stdin.readline

    a, b, x = map(int, input().split())
    print(f(b, x) - f(a - 1, x))


if __name__ == "__main__":
    main()
