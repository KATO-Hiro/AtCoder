# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    k = int(input())

    if k % 9 != 0:
        print(0)
        exit()

    mod = 10 ** 9 + 7
    dp = [0] * (k + 1)
    dp[0] = 1

    for i in range(1, k + 1):
        for j in range(1, min(i, 9) + 1):
            dp[i] += dp[i - j]

        dp[i] %= mod
    
    print(dp[k] % mod)


if __name__ == "__main__":
    main()
