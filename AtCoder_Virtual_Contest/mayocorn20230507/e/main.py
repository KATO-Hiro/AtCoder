# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    # 巡回セールマン問題っぽい
    n = int(input())
    xyz = [tuple(map(int, input().split())) for _ in range(n)]
    inf = 10 ** 18
    dp = [[inf for _ in range(n + 1)] for _ in range((1 << n) + 1)]
    dp[(1 << n) - 1][0] = 0
    dist = [[inf for _ in range(n)] for _ in range(n)]

    for i, (xi, yi, zi) in enumerate(xyz):
        for j, (xj, yj, zj) in enumerate(xyz):
            cost = abs(xj - xi) + abs(yj - yi) + max(0, zj - zi)
            dist[i][j] = min(dist[i][j], cost)

    for s in range((1 << n) - 2, -1, -1):
        for v in range(n):
            for u in range(n):
                if not (s >> u & 1):
                    dp[s][v] = min(dp[s][v], dp[s | 1 << u][u] + dist[v][u])
    
    print(dp[0][0])


if __name__ == "__main__":
    main()
