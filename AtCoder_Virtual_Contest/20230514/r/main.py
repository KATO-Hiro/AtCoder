# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k, d = map(int, input().split())
    a = list(map(int, input().split()))
    # dp[i][j][x]: i個からj個選んだときの和(mod d)の最大値
    dp = [[[-1 for _ in range(105)] for _ in range(105)] for _ in range(105)]
    dp[0][0][0] = 0

    for i in range(n):
        for j in range(i + 1):
            for x in range(d):
                if dp[i][j][x] == -1:
                    continue

                # aiを選ばない
                ni, nj, nx = i + 1, j, x % d
                dp[ni][nj][nx] = max(dp[ni][nj][nx], dp[i][j][x])

                # aiを選ぶ
                ni, nj, nx = i + 1, j + 1, (x + a[i]) % d
                dp[ni][nj][nx] = max(dp[ni][nj][nx], dp[i][j][x] + a[i])

    print(dp[n][k][0])


if __name__ == "__main__":
    main()
