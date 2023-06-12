# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = list(input().rstrip())
    t = list(input().rstrip())
    n, m = len(s), len(t)
    inf = 10**9
    dp = [[inf for _ in range(m + 1)] for _ in range(n + 1)]
    dp[0][0] = 0

    for i in range(n + 1):
        for j in range(m + 1):
            if i >= 1 and j >= 1:
                if s[i - 1] == t[j - 1]:
                    diff = 0
                else:
                    diff = 1

                dp[i][j] = min(
                    dp[i][j],
                    dp[i - 1][j] + 1,
                    dp[i][j - 1] + 1,
                    dp[i - 1][j - 1] + diff,
                )
            elif i >= 1:
                dp[i][j] = min(dp[i][j], dp[i - 1][j] + 1)
            elif j >= 1:
                dp[i][j] = min(dp[i][j], dp[i][j - 1] + 1)

    print(dp[n][m])


if __name__ == "__main__":
    main()
