# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, l, r = map(int, input().split())
    a = list(map(int, input().split()))
    dp = [0] * 3  # L, Ai, Rの3択
    inf = 10**18

    for i, ai in enumerate(a):
        add = [l, ai, r]
        ndp = [inf] * 3

        for j in range(3):
            for k in range(j, 3):
                ndp[k] = min(ndp[k], dp[j] + add[k])

        dp = ndp

    print(min(dp))


if __name__ == "__main__":
    main()
