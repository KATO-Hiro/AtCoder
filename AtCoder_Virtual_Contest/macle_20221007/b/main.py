# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    mod = 998244353
    dp = [1] * 10
    dp[0] = 0

    for i in range(2, n + 1):
        ndp = [0] * 10

        for j in range(1, 10):
            for k in range(j - 1, j + 2):
                if 1 <= k <= 9:
                    ndp[k] += dp[j]
                    ndp[k] %= mod

        dp = ndp
    
    print(sum(dp) % mod)


if __name__ == "__main__":
    main()
