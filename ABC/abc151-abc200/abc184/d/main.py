# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    a, b, c = map(int, input().split())
    n = 100
    dp = [[[0 for _ in range(n + 1)] for _ in range(n + 1)] for _ in range(n + 1)]

    for i in range(n - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            for k in range(n - 1, -1, -1):
                if i + j + k == 0:
                    continue

                expected_value = 0
                expected_value += dp[i + 1][j][k] * i
                expected_value += dp[i][j + 1][k] * j
                expected_value += dp[i][j][k + 1] * k

                dp[i][j][k] += expected_value / (i + j + k)
                dp[i][j][k] += 1

    print(dp[a][b][c])


if __name__ == "__main__":
    main()
