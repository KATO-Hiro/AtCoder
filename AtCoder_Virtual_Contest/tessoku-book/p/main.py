# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    inf = 10**9
    dp = [inf] * n
    dp[0] = 0

    for i in range(1, n):
        dp[i] = min(dp[i], dp[i - 1] + a[i - 1])

        if i >= 2:
            dp[i] = min(dp[i], dp[i - 2] + b[i - 2])

    print(dp[n - 1])


if __name__ == "__main__":
    main()
