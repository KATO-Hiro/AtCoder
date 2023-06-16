# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())

    # 体力・気力の下限値を全探索
    upper = 102
    dp = [[0 for _ in range(upper)] for _ in range(upper)]

    # 2次元累積和
    for _ in range(n):
        ai, bi = map(int, input().split())
        dp[ai][bi] += 1

    for i in range(1, upper):
        for j in range(1, upper):
            dp[i][j] += dp[i - 1][j]
            dp[i][j] += dp[i][j - 1]
            dp[i][j] -= dp[i - 1][j - 1]

    ans = 0
    k += 1

    for i in range(k, upper):
        for j in range(k, upper):
            x = dp[i][j]
            x -= dp[i - k][j]
            x -= dp[i][j - k]
            x += dp[i - k][j - k]

            ans = max(ans, x)

    print(ans)


if __name__ == "__main__":
    main()
