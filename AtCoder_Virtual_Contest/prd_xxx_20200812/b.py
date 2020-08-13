# -*- coding: utf-8 -*-


def main():
    n = int(input())
    dp = [float('inf') for _ in range(n + 100)]
    dp[0] = 0

    for i in range(1, n + 1):
        dp[i] = min(dp[i - 1] + 1, dp[i])

        six = 6

        while six <= i:
            dp[i] = min(dp[i - six] + 1, dp[i])
            six *= 6

        nine = 9

        while nine <= i:
            dp[i] = min(dp[i - nine] + 1, dp[i])
            nine *= 9

    print(dp[n])


if __name__ == '__main__':
    main()
