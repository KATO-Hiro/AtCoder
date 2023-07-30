# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = input().rstrip()
    n = len(s)
    ng = -1
    dp = [ng] * (n + 1)
    dp[0] = 1
    mod = 998244353

    for i, si in enumerate(s):
        ndp = [0] * (n + 1)

        for j in range(n + 1):
            if dp[j] == ng:
                continue

            if si == "(":
                if j + 1 <= n:
                    ndp[j + 1] += dp[j]
                    ndp[j + 1] %= mod
            elif si == ")":
                if j - 1 >= 0:
                    ndp[j - 1] += dp[j]
                    ndp[j - 1] %= mod
            else:
                if j + 1 <= n:
                    ndp[j + 1] += dp[j]
                    ndp[j + 1] %= mod

                if j - 1 >= 0:
                    ndp[j - 1] += dp[j]
                    ndp[j - 1] %= mod

        dp = ndp

    print(dp[0] % mod)


if __name__ == "__main__":
    main()
