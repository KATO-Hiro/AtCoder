# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    w = int(input())
    n, k = map(int, input().split())
    dp = [[0 for _ in range(w + 1)] for __ in range(k + 1)]
    ans = 0

    for index in range(n):
        ai, bi = map(int, input().split())

        for i in range(min(index + 1, k), 0, -1):
            for j in range(ai, w + 1):
                dp[i][j] = max(dp[i][j], dp[i - 1][j - ai] + bi)
                ans = max(ans, dp[i][j])

    print(ans)


if __name__ == "__main__":
    main()
