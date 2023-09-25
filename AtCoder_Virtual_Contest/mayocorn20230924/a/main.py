# -*- coding: utf-8 -*-


def main():
    import sys
    from math import sqrt

    input = sys.stdin.readline

    n = int(input())
    x = list(map(int, input().split()))
    a, b, c = 0, 0, 0

    for xi in x:
        a += abs(xi)
        b += xi**2
        c = max(c, abs(xi))

    print(a)
    print(sqrt(b))
    print(c)


if __name__ == "__main__":
    main()
