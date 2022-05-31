# -*- coding: utf-8 -*-


def calc_line_passing_through(point1, point2):
    '''
    Args:
        point1, point2: Points that constitutes a line.

    Returns:
        parameters of the line.
            slope    : a, b
            intercept: c
    Landau notation: O(log(min(a, b, c))).

    See:
    https://atcoder.jp/contests/abc248/submissions/31018608
    '''

    from math import gcd

    a = point2[1] - point1[1]
    b = point1[0] - point2[0]
    c = -(point1[0] * a + point1[1] * b)

    if a < 0:
        a, b, c = -a, -b, -c

    if a == 0 and b < 0:
        b, c = -b, -c

    g = gcd(gcd(a, b), c)
    a //= g
    b //= g
    c //= g

    return (a, b, c)


def main():
    from collections import defaultdict
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    xy = [tuple(map(int, input().split())) for _ in range(n)]
    d = defaultdict(int)

    if k == 1:
        print("Infinity")
        exit()

    for i in range(n):
        for j in range(i + 1, n):
            result = calc_line_passing_through(xy[i], xy[j])
            d[result] += 1
    
    ans = 0
    
    for value in d.values():
        if value >= k * (k - 1) // 2:
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
