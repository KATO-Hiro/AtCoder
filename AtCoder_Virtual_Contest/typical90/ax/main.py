# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, l = map(int, input().split())
    dp = [0] * (n + 1)
    dp[0] = 1
    mod = 10**9 + 7

    for i in range(n):
        if i + 1 <= n:
            dp[i + 1] += dp[i]
            dp[i + 1] %= mod
        if i + l <= n:
            dp[i + l] += dp[i]
            dp[i + l] %= mod

    print(dp[n])


if __name__ == "__main__":
    main()
