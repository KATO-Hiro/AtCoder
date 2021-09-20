# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    x, y = map(int, input().split())
    inf = n + 1
    dp = [[inf for _ in range(y + 1)] for __ in range(x + 1)]
    dp[0][0] = 0

    for _ in range(n):
        ai, bi = map(int, input().split())

        for j in range(x, -1, -1):
            for k in range(y, -1, -1):
                xi = min(j + ai, x)
                yi = min(k + bi, y)
                dp[xi][yi] = min(dp[xi][yi], dp[j][k] + 1)

    ans = dp[x][y]

    if ans == inf:
        print(-1)
    else:
        print(ans)


if __name__ == "__main__":
    main()