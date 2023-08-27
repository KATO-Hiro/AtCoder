# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import accumulate

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    size = 3001
    dp = [0] * size
    dp[0] = 1
    mod = 998244353

    for ai, bi in zip(a, b):
        ndp = [0] * size
        dp = list(accumulate(dp))

        for j in range(ai, bi + 1):
            ndp[j] = dp[j]
            ndp[j] %= mod

        dp = ndp

    print(sum(dp) % mod)


if __name__ == "__main__":
    main()
