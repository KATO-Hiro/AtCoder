# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import pairwise

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    x, y = 0, 0

    for ai, aj in pairwise(a):
        if ai < aj:
            x += aj - ai
        else:
            y += ai - aj

    print(x, y)


if __name__ == "__main__":
    main()
