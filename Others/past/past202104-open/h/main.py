# -*- coding: utf-8 -*-


def main():
    from itertools import accumulate
    from math import ceil
    import sys

    input = sys.stdin.readline

    n, m, k, q = map(int, input().split())
    a = list()
    b = list()

    for i in range(n):
        pi, ti = map(int, input().split())

        if ti == 0:
            a.append(pi)
        else:
            b.append(pi)
    
    a_size = len(a)
    a = list(accumulate([0] + sorted(a)))
    b = list(accumulate([0] + sorted(b)))
    ans = float("inf")

    for i, bi in enumerate(b):
        j = m - i
        cost = 0

        if 0 <= j <= a_size:
            cost += a[j]
            cost += bi
            cost += ceil(i / k) * q

            ans = min(ans, cost)
    
    print(ans)


if __name__ == "__main__":
    main()
