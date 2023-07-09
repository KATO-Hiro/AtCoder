# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict

    input = sys.stdin.readline

    n, k = map(int, input().split())
    d = defaultdict(int)

    # imos法
    for _ in range(n):
        ai, bi = map(int, input().split())
        d[1] += bi
        d[1 + ai] -= bi

    days = sorted(d.keys())

    for k1, k2 in zip(days, days[1:]):
        d[k2] += d[k1]

    for day in days:
        count = d[day]

        if count <= k:
            print(day)
            exit()


if __name__ == "__main__":
    main()
