# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    ab = [tuple(map(int, input().split())) for _ in range(n)]
    dp = [1, 1]
    mod = 998244353

    for i in range(n - 1):
        ai, bi = ab[i]
        ani, bni = ab[i + 1]
        ndp = [0, 0]

        # 表 to 表
        if ai != ani:
            ndp[0] += dp[0]
            ndp[0] %= mod

        # 表 to 裏
        if ai != bni:
            ndp[1] += dp[0]
            ndp[1] %= mod

        # 裏 to 表
        if bi != ani:
            ndp[0] += dp[1]
            ndp[0] %= mod

        # 裏 to 裏
        if bi != bni:
            ndp[1] += dp[1]
            ndp[1] %= mod

        dp = ndp

    print(sum(dp) % mod)


if __name__ == "__main__":
    main()
