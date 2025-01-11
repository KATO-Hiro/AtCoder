# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import pairwise
    from math import gcd, sqrt

    input = sys.stdin.readline

    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    g = set()

    for ai, aj in pairwise(a):
        g.add(aj - ai)

    d_gcd = gcd(*list(g))
    e = set()

    for i in range(1, int(sqrt(d_gcd) + 1)):
        if d_gcd % i != 0:
            continue

        e.add(i)
        e.add(d_gcd // i)

    c = [ai - a[0] for ai in a]
    c_max = max(c)
    ans = set()

    for ei in e:
        if (n - 1) * ei >= c_max:
            ans.add(ei)

    print(len(ans))
    print(*sorted(ans))


if __name__ == "__main__":
    main()
