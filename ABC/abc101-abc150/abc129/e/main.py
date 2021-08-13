# -*- coding: utf-8 -*-


def main():
    l = list(input())
    n = len(l)
    mod = 10 ** 9 + 7
    dp = [[0 for _ in range(2)] for _ in range(n + 10)]
    dp[0][0] = 1

    for i, li in enumerate(l):
        # a + b = 0
        if li == '0':
            dp[i + 1][0] = dp[i][0]
            dp[i + 1][1] = dp[i][1]
        else:
            dp[i + 1][1] = dp[i][0] + dp[i][1]
            dp[i + 1][1] %= mod

        # a + b = 1
        if li == '0':
            dp[i + 1][1] += dp[i][1] * 2
            dp[i + 1][1] %= mod
        else:
            dp[i + 1][0] += dp[i][0] * 2
            dp[i + 1][0] %= mod
            dp[i + 1][1] += dp[i][1] * 2
            dp[i + 1][1] %= mod

    ans = dp[n][0] + dp[n][1]
    ans %= mod
    print(ans)


if __name__ == "__main__":
    main()
