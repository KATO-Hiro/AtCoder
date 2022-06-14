# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    mod = 998244353
    dp = [0] * 10
    dp[a[0]] = 1

    for i in range(1, n):
        ndp = [0] * 10
        cur = a[i]

        for j in range(10):
            ndp[(j + cur) % 10] += dp[j]
            ndp[(j * cur) % 10] += dp[j]

        for j in range(10):
            ndp[j] %= mod

        dp = ndp
    
    for i in range(10):
        dp[i] %= mod
        print(dp[i])


if __name__ == "__main__":
    main()
