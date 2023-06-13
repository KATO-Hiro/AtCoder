# -*- coding: utf-8 -*-


def main():
    import sys
    from math import sqrt

    input = sys.stdin.readline

    n = int(input())
    xy = [tuple(map(int, input().split())) for _ in range(n)]
    inf = 10**12
    dist = [[inf for _ in range(n)] for _ in range(n)]

    for i in range(n):
        xi, yi = xy[i]

        for j in range(n):
            xj, yj = xy[j]

            dist[i][j] = sqrt((xi - xj) ** 2 + (yi - yj) ** 2)

    dp = [[inf for _ in range(n)] for _ in range(1 << n)]
    dp[0][0] = 0

    for s in range(1 << n):
        for v in range(n):
            if dp[s][v] == inf:
                continue

            for u in range(n):
                if not ((s >> u) & 1):
                    dp[s | 1 << u][u] = min(dp[s | 1 << u][u], dp[s][v] + dist[v][u])

    print(dp[(1 << n) - 1][0])


if __name__ == "__main__":
    main()
