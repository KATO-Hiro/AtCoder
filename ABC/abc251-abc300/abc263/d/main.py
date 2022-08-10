# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, l, r = map(int, input().split())
    a = list(map(int, input().split()))
    inf = 10 ** 15
    dp = [l, a[0], r]  # L、Ai、Rを選択したときの総和の最小値

    for i in range(1, n):
        ndp = [inf] * 3

        # L → L
        ndp[0] = min(ndp[0], dp[0] + l)
        # L → Ai
        ndp[1] = min(ndp[1], dp[0] + a[i])

        # Ai → Ai
        ndp[1] = min(ndp[1], dp[1] + a[i])
        # Ai → R
        ndp[2] = min(ndp[2], dp[1] + r)

        # R → R
        ndp[2] = min(ndp[2], dp[2] + r)

        dp = ndp

    print(min(dp))


if __name__ == "__main__":
    main()
