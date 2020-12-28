# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    h, w = map(int, input().split())
    s = [input().rstrip() for _ in range(h)]

    mod = 10 ** 9 + 7

    dp = [[0 for __ in range(w + 1)] for _ in range(h + 1)]
    x = [[0 for __ in range(w + 1)] for _ in range(h + 1)]
    y = [[0 for __ in range(w + 1)] for _ in range(h + 1)]
    z = [[0 for __ in range(w + 1)] for _ in range(h + 1)]
    dp[0][0] = 1

    for i in range(h):
        for j in range(w):
            if i == 0 and j == 0:
                continue

            if s[i][j] == "#":
                continue

            if j > 0:
                x[i][j] = (x[i][j - 1] + dp[i][j - 1]) % mod
            if i > 0:
                y[i][j] = (y[i - 1][j] + dp[i - 1][j]) % mod
            if i > 0 and j > 0:
                z[i][j] = (z[i - 1][j - 1] + dp[i - 1][j - 1]) % mod

            dp[i][j] = (x[i][j] + y[i][j] + z[i][j]) % mod

    print(dp[h - 1][w - 1])


if __name__ == "__main__":
    main()
