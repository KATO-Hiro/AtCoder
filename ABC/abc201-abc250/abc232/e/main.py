# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    h, w, k = map(int, input().split())
    sx, sy, tx, ty = map(int, input().split())
    dp = [[0] * 2 for _ in range(2)]
    dp[sx == tx][sy == ty] = 1
    mod = 998244353

    for _ in range(k):
        ndp = [[0] * 2 for _ in range(2)]

        for j in range(2):
            ndp[0][j] += dp[0][j] * (h - 2)
            ndp[1][j] += dp[0][j]
            ndp[1][j] %= mod
            ndp[0][j] += dp[1][j] * (h - 1)
            ndp[0][j] %= mod

        for i in range(2):
            ndp[i][0] += dp[i][0] * (w - 2)
            ndp[i][1] += dp[i][0]
            ndp[i][1] %= mod
            ndp[i][0] += dp[i][1] * (w - 1)
            ndp[i][0] %= mod

        dp = ndp
    
    print(dp[1][1] % mod)


if __name__ == "__main__":
    main()
