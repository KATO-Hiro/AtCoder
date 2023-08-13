# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    a, b = map(int, input().split())
    grid = [[1 for _ in range(a)] for _ in range(b)]
    dp = [[0 for _ in range(a)] for _ in range(b)]
    dp[0][0] = 1
    n = int(input())

    for _ in range(n):
        xi, yi = map(int, input().split())
        xi -= 1
        yi -= 1
        grid[yi][xi] = -1

    for j in range(a):
        for i in range(b):
            if grid[i][j] == -1:
                continue

            if i - 1 >= 0:
                dp[i][j] += dp[i - 1][j]
            if j - 1 >= 0:
                dp[i][j] += dp[i][j - 1]

    print(dp[b - 1][a - 1])


if __name__ == "__main__":
    main()
