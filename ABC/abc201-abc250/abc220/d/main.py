# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    dp = [0] * 10
    mod = 998244353

    x, y = a[0], a[1]
    z = (x + y) % 10
    dp[z] += 1
    z = (x * y) % 10
    dp[z] += 1

    for i in range(2, n):
        ndp = [0] * 10

        for index, d in enumerate(dp):
            if d == 0:
                continue

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
