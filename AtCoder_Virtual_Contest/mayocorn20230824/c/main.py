# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    mod = 998244353
    dp = [1] * 10
    dp[0] = 0

    for i in range(n - 1):
        ndp = [0] * 10

        for j in range(1, 10):
            if j - 1 >= 1:
                ndp[j - 1] += dp[j]
                ndp[j - 1] %= mod

            ndp[j] += dp[j]
            ndp[j] %= mod

            if j + 1 <= 9:
                ndp[j + 1] += dp[j]
                ndp[j + 1] %= mod

        dp = ndp

    print(sum(dp) % mod)


if __name__ == "__main__":
    main()
