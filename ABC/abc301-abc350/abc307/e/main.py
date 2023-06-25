# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    mod = 998244353

    # dp[i][j]: i番目の人の数字jを決めたときに、隣り合う人の数が異なる数(mod 998244353)
    # 先頭の数字を決め打ちしてみる
    # 高速化: jを区別しない => 先頭の人と一致するかどうか?
    # 人1の数字を決め打ちしたときに、i番目の人が一致しているか(False / True)?
    dp = [0, m]

    for _ in range(n - 1):
        ndp = [0] * 2

        ndp[0] = dp[0] * (m - 2) + dp[1] * (m - 1)
        ndp[0] %= mod
        ndp[1] = dp[0] * 1
        ndp[1] %= mod

        dp = ndp

    print(dp[0])


if __name__ == "__main__":
    main()
