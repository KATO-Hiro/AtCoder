# -*- coding: utf-8 -*-

from math import gcd


def calc_line_passing_through(point1, point2):
    """

    Args:
        point1, point2: Points that constitutes a line.

    Returns:
        parameters of the line.
            slope    : a, b
            intercept: c

    Landau notation: O(log(min(a, b, c))).

    See:
    https://atcoder.jp/contests/abc248/submissions/31018608
    """

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

    return (a, b, g)


def main():
    import sys
    from collections import defaultdict

    input = sys.stdin.readline

    n = int(input())
    xy = [tuple(map(int, input().split())) for _ in range(n)]
    d = defaultdict(list)

    for i in range(n):
        for j in range(i + 1, n):
            a, b, g = calc_line_passing_through(xy[i], xy[j])
            d[(a, b)].append(g)

    ans = 0

    # See
    # https://atcoder.jp/contests/abc418/submissions/68330674
    for _, values in d.items():
        size = len(values)
        ans += size * (size - 1)  # 順序ありのペア

        # 同じ辺の長さの場合を重複している数えているので除外
        duplicates = defaultdict(int)

        for value in values:
            duplicates[value] += 1

        for duplicate in duplicates.values():
            ans -= duplicate * (duplicate - 1) // 2

    print(ans // 2)


if __name__ == "__main__":
    main()
