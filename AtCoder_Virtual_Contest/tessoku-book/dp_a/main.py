# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    h = list(map(int, input().split()))
    inf = 10**12
    dp = [inf] * (n + 10)
    dp[0] = 0

    for i in range(n):
        if i - 1 >= 0:
            dp[i] = min(dp[i], dp[i - 1] + abs(h[i] - h[i - 1]))
        if i - 2 >= 0:
            dp[i] = min(dp[i], dp[i - 2] + abs(h[i] - h[i - 2]))

    print(dp[n - 1])


if __name__ == "__main__":
    main()
