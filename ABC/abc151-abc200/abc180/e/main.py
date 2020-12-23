# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    xyz = [tuple(map(int, input().split())) for _ in range(n)]
    dist = [[10 ** 8 for __ in range(n)] for _ in range(n)]

    for i, (x1, y1, z1) in enumerate(xyz):
        for j, (x2, y2, z2) in enumerate(xyz):
            dist[i][j] = abs(x2 - x1) + abs(y2 - y1) + max(0, z2 - z1)

    dp = [[10 ** 8 for __ in range(n)] for _ in range(1 << n)]
    dp[(1 << n) - 1][0] = 0

    for si in range((1 << n) - 2, -1, -1):
        for v in range(n):
            for u in range(n):
                if not (si >> u & 1):
                    dp[si][v] = min(dp[si][v], dp[si | (1 << u)][u] + dist[v][u])

    print(dp[0][0])


if __name__ == "__main__":
    main()
