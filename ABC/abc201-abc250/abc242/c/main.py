# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = input()
    n = int(s)
    mod = 998244353 
    dp = [1] * 10

    for i in range(2, n + 1):
        ndp = [0] * 10

        for j in range(1, 10):
            for k in [-1, 0, 1]:
                if 1 <= j + k <= 9:
                    ndp[j + k] += dp[j]
                    ndp[j + k] %= mod
        
        dp = ndp
    
    print(sum(dp) % mod)


if __name__ == "__main__":
    main()
