# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    inf = 10**6
    dp = [inf] * (n + 1)
    dp[0] = 0

    for i in range(1, n + 1):
        dp[i] = min(dp[i], dp[i - 1] + 1)
        six, nine = 6, 9

        while i - six >= 0:
            dp[i] = min(dp[i], dp[i - six] + 1)
            six *= 6

        while i - nine >= 0:
            dp[i] = min(dp[i], dp[i - nine] + 1)
            nine *= 9

    print(dp[n])


if __name__ == "__main__":
    main()
