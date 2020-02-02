# -*- coding: utf-8 -*-


def calc_dist(x1, y1, x2, y2):
    return (x2 - x1) ** 2 + (y2 - y1) ** 2


def main():
    from itertools import combinations
    from math import sqrt

    n, m = map(int, input().split())
    a = list()
    b = list()
    ans = float('inf')

    if n > 0:
        for i in range(n):
            xi, yi, ri = map(int, input().split())
            ans = min(ans, ri)
            a.append((xi, yi, ri))

    for j in range(m):
        xi, yi = map(int, input().split())
        b.append((xi, yi))

    if m > 1:
        dist = float('inf')

        for (x1, y1), (x2, y2) in list(combinations(b, 2)):
            dist = min(dist, calc_dist(x1, y1, x2, y2))

        ans = min(ans, sqrt(dist) / 2)

    if n > 0 and m > 0:
        dist = float('inf')

        for xa, ya, ra in a:
            for xb, yb in b:
                dist = min(dist, sqrt(calc_dist(xa, ya, xb, yb)) - ra)
        ans = min(ans, dist)

    print(ans)


if __name__ == '__main__':
    main()
