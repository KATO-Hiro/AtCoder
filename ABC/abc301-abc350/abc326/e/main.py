# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = [0] + list(map(int, input().split()))
    dp = [0] * (n + 1)
    mod = 998244353
    inv = pow(n, -1, mod)  # 1 / p
    summed = 0

    # 愚直なDP -> 累積和で高速化
    for i in range(n, -1, -1):
        dp[i] = summed * inv + a[i]
        dp[i] %= mod

        summed += dp[i]
        summed %= mod

    print(dp[0])


if __name__ == "__main__":
    main()
