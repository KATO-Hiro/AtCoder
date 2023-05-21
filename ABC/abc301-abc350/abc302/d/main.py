# -*- coding: utf-8 -*-


def main():
    import sys
    from bisect import bisect

    input = sys.stdin.readline

    n, m, d = map(int, input().split())
    a = list(map(int, input().split()))
    b = sorted(list(map(int, input().split())))
    inf = 10**20
    c = [-inf] + b + [inf]
    ans = -1

    for ai in a:
        i1 = bisect(c, ai - d)
        i2 = bisect(c, ai + d)

        for x in range(max(0, i1 - 2), min(i1 + 2, m + 2)):
            if abs(ai - c[x]) <= d:
                ans = max(ans, ai + c[x])

        for y in range(max(0, i2 - 2), min(i2 + 2, m + 2)):
            if abs(ai - c[y]) <= d:
                ans = max(ans, ai + c[y])

    print(ans)


if __name__ == "__main__":
    main()
