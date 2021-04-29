# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = input().rstrip()
    dp = [[0 for _ in range(n + 5)] for _ in range(n + 5)]

    for i in range(n - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j + 1] + 1

    ans = 0

    for i in range(n):
        for j in range(n):
            if i >= j:
                continue

            candidate = min(j - i, dp[i][j])
            ans = max(ans, candidate)

    print(ans)


if __name__ == "__main__":
    main()
