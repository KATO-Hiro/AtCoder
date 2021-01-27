# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    r = list(map(int, input().split()))
    dp = [[0 for _ in range(2 * n + 10)] for _ in range(2)]
    ans = 0

    for i in range(n):
        dp[0][i + 1] = 1
        dp[1][i + 1] = 1

        for j in range(i):
            if r[j] < r[i]:
                dp[1][i + 1] = max(dp[1][i + 1], dp[0][j + 1] + 1)

            if r[j] > r[i]:
                dp[0][i + 1] = max(dp[0][i + 1], dp[1][j + 1] + 1)

        ans = max(ans, dp[0][i + 1], dp[1][i + 1])

    if ans < 3:
        ans = 0

    print(ans)


if __name__ == "__main__":
    main()
