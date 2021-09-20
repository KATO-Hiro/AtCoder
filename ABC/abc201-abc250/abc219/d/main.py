# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    x, y = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n)]
    inf = 10 ** 9
    size_max = 305
    dp = [[[inf for _ in range(size_max + 1)] for __ in range(size_max + 1)] for ___ in range(size_max + 1)]
    dp[0][0][0] = 0

    for i in range(n):
        ai, bi = ab[i]

        for j in range(x + 1):
            for k in range(y + 1):
                dp[i + 1][j][k] = min(dp[i + 1][j][k], dp[i][j][k])

                xi = min(j + ai, x)
                yi = min(k + bi, y)

                dp[i + 1][xi][yi] = min(dp[i + 1][xi][yi], dp[i][j][k] + 1)

    ans = dp[n][x][y]

    if ans == inf:
        print(-1)
    else:
        print(ans)


if __name__ == "__main__":
    main()