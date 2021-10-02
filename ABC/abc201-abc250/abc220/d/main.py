# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    dp = [0] * 10
    mod = 998244353
    dp[a[0]] = 1

    for i in range(1, n):
        ndp = [0] * 10

        for index, d in enumerate(dp):
            z = (index + a[i]) % 10
            ndp[z] += d
            ndp[z] %= mod
            z = (index * a[i]) % 10
            ndp[z] += d
            ndp[z] %= mod

        dp = ndp
    
    print('\n'.join(map(str, dp)))


if __name__ == "__main__":
    main()
