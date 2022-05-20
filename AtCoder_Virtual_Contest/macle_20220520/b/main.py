# -*- coding: utf-8 -*-


def f(x, a, b):
    from math import floor

    return floor(a * x / b)


def main():
    import sys

    input = sys.stdin.readline

    a, b, n = map(int, input().split())

    if n < b:
        print(f(n, a, b))
    else: 
        print(f(b - 1, a, b))
    


if __name__ == "__main__":
    main()
