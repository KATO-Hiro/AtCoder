# -*- coding: utf-8 -*-


def dist(x1, y1, x2, y2):
    from math import sqrt

    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def main():
    import sys
    from itertools import pairwise

    input = sys.stdin.readline

    n = int(input())
    xy = [(0, 0)] + [tuple(map(int, input().split())) for _ in range(n)] + [(0, 0)]
    ans = 0

    for (x1, y1), (x2, y2) in pairwise(xy):
        ans += dist(x1, y1, x2, y2)

    print(ans)


if __name__ == "__main__":
    main()
