# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    t = list(map(int, input().split()))
    inf = 10 ** 7
    m = 10 ** 5 + 3000
    dp = [[inf for _ in range(m)] for __ in range(n + 10)]
    dp[0][0] = 0

    for i in range(n):
        for j in range(101001):
            # Use 1st
            dp[i + 1][j + t[i]] = min(dp[i][j], dp[i + 1][j + t[i]])

            # Use 2nd
            dp[i + 1][j] = min(dp[i][j] + t[i], dp[i + 1][j])

    total = sum(t)
    ans = float("inf")

    for t in range(101001):
        ans = min(ans, max(dp[n][t], total - dp[n][t]))

    print(ans)


if __name__ == "__main__":
    main()
