# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = int(input())
    s_max = 2001
    dp = [1 for _ in range(s_max)]
    dp[0], dp[1], dp[2] = 0, 0, 0
    mod = 10 ** 9 + 7

    for i in range(3, s + 1):
        for j in range(3, s + 1):
            if i + j <= s:
                dp[i + j] += dp[i]
                dp[i + j] %= mod

    print(dp[s])


if __name__ == "__main__":
    main()
