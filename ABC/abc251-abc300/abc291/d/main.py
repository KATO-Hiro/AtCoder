# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    ab = list()
    ab.append((0, 0))

    for _ in range(n):
        ai, bi = map(int, input().split())
        ab.append((ai, bi))
    
    dp = [0, 1]
    mod = 998244353

    for i in range(1, n + 1):
        ndp = [0, 0]

        ai, bi = ab[i]
        aj, bj = ab[i - 1]

        if ai != aj:
            ndp[0] += dp[0]
        if ai != bj:
            ndp[0] += dp[1]
        if bi != aj:
            ndp[1] += dp[0]
        if bi != bj:
            ndp[1] += dp[1]

        ndp[0] %= mod
        ndp[1] %= mod

        dp = ndp

    print(sum(dp) % mod)
    

if __name__ == "__main__":
    main()
