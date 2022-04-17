# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m, k = map(int, input().split())
    size = n * m + 10
    dp = [0 for _ in range(size)]
    mod = 998244353

    for i in range(m):
        dp[i] = 1

    for i in range(n - 1):
        ndp = [0 for _ in range(size)]

        for j in range(k + 1):
            for x in range(1, m + 1):
                if j + x >= k:
                    continue

                ndp[j + x] += dp[j]
                ndp[j + x] %= mod
        
        dp = ndp
    
    print(sum(dp) % mod)


if __name__ == "__main__":
    main()
