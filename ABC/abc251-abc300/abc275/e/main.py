# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m, k = map(int, input().split())
    dp = [0] * (n + 1)
    dp[0] = 1
    mod = 998244353
    # 1 / m: modの世界における逆元を取ることで、割り算を掛け算の形に
    inv = pow(m, mod - 2, mod)

    for _ in range(k):
        ndp = [0] * (n + 1)

        # 既にゴールに到達
        ndp[n] = dp[n]

        for i in range(n):
            for j in range(1, m + 1):
                if i + j > n:
                    ni = n - (i + j - n)
                else:
                    ni = i + j
                
                ndp[ni] += dp[i] * inv
                ndp[ni] %= mod
        
        dp = ndp

    print(dp[n])


if __name__ == "__main__":
    main()
