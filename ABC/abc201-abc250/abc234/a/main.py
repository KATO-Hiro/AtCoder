# -*- coding: utf-8 -*-


def f(x):
    return x ** 2 + 2 * x + 3


def main():
    import sys

    input = sys.stdin.readline

    t = int(input())
    print(f(f(f(t) + t) + f(f(t))))


if __name__ == "__main__":
    main()
