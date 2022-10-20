# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m, k = map(int, input().split())
    k_max = n * m + 1
    dp = [0] * k_max
    dp[0] = 1
    mod = 998244353

    for j in range(n):
        ndp = [0] * k_max

        for i in range(k_max):
            for ai in range(1, m + 1):
                if i + ai <= k:
                    ndp[i + ai] += dp[i]
                    ndp[i + ai] %= mod
        
        dp = ndp
    
    print(sum(dp) % mod)


if __name__ == "__main__":
    main()
