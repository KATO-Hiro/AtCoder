# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    ab = [tuple(map(int, input().split())) for _ in range(n)]
    dp = [1, 1]
    mod = 998244353

    for i in range(1, n):
        a1, b1 = ab[i - 1]
        a2, b2 = ab[i]
        ndp = [0, 0]

        if a1 != a2:
            ndp[0] += dp[0]
        if a1 != b2:
            ndp[1] += dp[0]
        if b1 != a2:
            ndp[0] += dp[1]
        if b1 != b2:
            ndp[1] += dp[1]

        ndp[0] %= mod
        ndp[1] %= mod

        dp = ndp
    
    print(sum(dp) % mod)


if __name__ == "__main__":
    main()
