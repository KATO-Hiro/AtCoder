# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    dp = [
        [[0 for _ in range(h + w + 10)] for _ in range(w + 10)] for _ in range(h + 10)
    ]
    dp[0][0][1] = a[0][0]

    for i in range(h):
        for j in range(w):
            for k in range(h + w):
                # 取らない
                dp[i + 1][j][k] = max(dp[i + 1][j][k], dp[i][j][k])
                dp[i][j + 1][k] = max(dp[i][j + 1][k], dp[i][j][k])

                # 取る
                if i + 1 < h:
                    dp[i + 1][j][k + 1] = max(
                        dp[i + 1][j][k + 1], dp[i][j][k] + a[i + 1][j]
                    )

                if j + 1 < w:
                    dp[i][j + 1][k + 1] = max(
                        dp[i][j + 1][k + 1], dp[i][j][k] + a[i][j + 1]
                    )

    for i in range(1, h + w):
        print(dp[h - 1][w - 1][i])


if __name__ == "__main__":
    main()
