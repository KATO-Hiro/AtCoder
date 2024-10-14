# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import pairwise
    from math import hypot

    input = sys.stdin.readline

    n = int(input())
    xy = [(0, 0)] + [tuple(map(int, input().split())) for _ in range(n)] + [(0, 0)]
    ans = 0

    for (x1, y1), (x2, y2) in pairwise(xy):
        ans += hypot(x2 - x1, y2 - y1)

    print(ans)


if __name__ == "__main__":
    main()
