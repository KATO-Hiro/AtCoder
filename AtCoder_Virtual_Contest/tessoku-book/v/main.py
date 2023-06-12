# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    dp = [-1] * (n + 1)
    dp[0] = dp[1] = 0

    for i in range(n - 1):
        ai, bi = a[i], b[i]

        if dp[i + 1] == -1:
            continue

        dp[ai] = max(dp[ai], dp[i + 1] + 100)
        dp[bi] = max(dp[bi], dp[i + 1] + 150)

    print(dp[n])


if __name__ == "__main__":
    main()
