# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import pairwise
    from math import gcd

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    g = 0

    for a, b in pairwise(a):
        g = gcd(g, abs(b - a))

    if g == 1:
        print(2)
    else:
        print(1)


if __name__ == "__main__":
    main()
