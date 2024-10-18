# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    ab = [tuple(map(int, input().split())) for _ in range(n)]
    x = 0

    for _, bi in ab:
        x += bi

    if x % 3 != 0:
        print(-1)
        exit()

    x //= 3

    # 部分和問題 = DP
    inf = 10**12
    dp = [[inf for _ in range(x + 1)] for _ in range(x + 1)]
    dp[0][0] = 0

    for ai, bi in ab:
        ndp = [[inf for _ in range(x + 1)] for _ in range(x + 1)]

        # 元のチームと異なる場合にコストを加算
        cost1 = 0 if ai == 1 else 1
        cost2 = 0 if ai == 2 else 1
        cost3 = 0 if ai == 3 else 1

        # 3チーム目は残りの2チームで決まるため、状態を持たなくてもよい
        for j1 in range(x + 1):
            for j2 in range(x + 1):
                nj1, nj2 = j1 + bi, j2 + bi

                if nj1 <= x:
                    ndp[nj1][j2] = min(ndp[nj1][j2], dp[j1][j2] + cost1)
                if nj2 <= x:
                    ndp[j1][nj2] = min(ndp[j1][nj2], dp[j1][j2] + cost2)

                ndp[j1][j2] = min(ndp[j1][j2], dp[j1][j2] + cost3)

        dp = ndp[:]

    if dp[x][x] == inf:
        print(-1)
    else:
        print(dp[x][x])


if __name__ == "__main__":
    main()
