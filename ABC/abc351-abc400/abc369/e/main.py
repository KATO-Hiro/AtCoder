# -*- coding: utf-8 -*-


def warshall_floyd(dist):
    """
    Args:
        Distance matrix between two points.

    Returns:
        Matrix of shortest distance.

    Landau notation: O(n ** 3).
    """

    v_count = len(dist[0])

    for k in range(v_count):
        for i in range(v_count):
            for j in range(v_count):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist


def main():
    import sys
    from itertools import permutations, product

    input = sys.stdin.readline

    n, m = map(int, input().split())
    inf = 10**18
    graph = [[inf for _ in range(n)] for _ in range(n)]

    # 対角は0
    for i in range(n):
        graph[i][i] = 0

    uvt = list()

    for _ in range(m):
        ui, vi, ti = map(int, input().split())
        ui -= 1
        vi -= 1
        uvt.append((ui, vi, ti))
        graph[ui][vi] = min(graph[ui][vi], ti)
        graph[vi][ui] = min(graph[vi][ui], ti)

    # 前計算
    dist = warshall_floyd(graph)
    # print(dist)
    q = int(input())

    # K! * 2 ^ Kパターンを全て試す
    for _ in range(q):
        ki = int(input())
        b = list(map(lambda x: int(x) - 1, input().split()))
        ans = inf

        for pattern in permutations(b):
            for bit in range(1 << ki):
                prev_vi = 0
                cost = 0

                for i, pi in enumerate(pattern):
                    ui, vi, ti = uvt[pi]

                    if (bit >> i) & 1:
                        ui, vi = vi, ui

                    cost += dist[prev_vi][ui]
                    cost += ti

                    prev_vi = vi

                cost += dist[prev_vi][n - 1]

                ans = min(ans, cost)

        print(ans)


if __name__ == "__main__":
    main()
