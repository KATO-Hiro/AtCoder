# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    w, h = map(int, input().split())
    size = 110

    # See:
    # https://atcoder.jp/contests/joi2010yo/submissions/16464228
    # https://atcoder.jp/contests/joi2010yo/submissions/10320279
    # dp[i][j][k1][k2]: マス(i, j)にいて、直近の2回の移動方向がk1→k2となる経路数 (mod 10 ** 5)
    # 右: 0、上: 1
    dp = [
        [[[0 for _ in range(2)] for _ in range(2)] for _ in range(size)]
        for _ in range(size)
    ]
    mod = 10**5

    # グリッドの端部から移動できる
    for i in range(1, h + 1):
        dp[i][1][1][1] = 1

    for j in range(1, w + 1):
        dp[1][j][0][0] = 1

    for j in range(2, w + 1):
        for i in range(2, h + 1):
            # 上方向へ
            dp[i][j][1][1] += dp[i - 1][j][1][1] + dp[i - 1][j][0][1]
            dp[i][j][1][1] %= mod
            dp[i][j][0][1] += dp[i - 1][j][0][0]
            dp[i][j][0][1] %= mod

            # 右方向へ
            dp[i][j][0][0] += dp[i][j - 1][0][0] + dp[i][j - 1][1][0]
            dp[i][j][0][0] %= mod
            dp[i][j][1][0] += dp[i][j - 1][1][1]
            dp[i][j][1][0] %= mod

    ans = 0

    for k1 in range(2):
        for k2 in range(2):
            ans += dp[h][w][k1][k2]
            ans %= mod

    print(ans)


if __name__ == "__main__":
    main()
