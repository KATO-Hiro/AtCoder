# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    inf = 10**9
    dp = [inf] * (10**6 + 10)
    dp[0] = 0

    for i in range(1, n + 1):
        first, second = 1, 1

        while True:
            if first > i:
                break

            dp[i] = min(dp[i], dp[i - first] + 1)
            first *= 6

        while True:
            if second > i:
                break

            dp[i] = min(dp[i], dp[i - second] + 1)
            second *= 9

    print(dp[n])


if __name__ == "__main__":
    main()
