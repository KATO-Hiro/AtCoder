# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    dp = [0] * 10
    dp[a[0]] = 1
    mod = 998244353

    for i in range(1, n):
        ndp = [0] * 10

        for j in range(10):
            ndp[(j + a[i]) % 10] += dp[j]
            ndp[(j * a[i]) % 10] += dp[j]
        
        for i in range(10):
            ndp[i] %= mod

        dp = ndp
    
    print(*dp, sep="\n")


if __name__ == "__main__":
    main()
