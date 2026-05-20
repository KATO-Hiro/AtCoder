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

    input = sys.stdin.readline

    n, m, k = map(int, input().split())
    inf = 10**18
    graph = [[inf for _ in range(m)] for _ in range(m)]

    for _ in range(k):
        ui, vi, wi = map(int, input().split())
        ui -= 1
        vi -= 1
        graph[ui][vi] = wi
        graph[vi][ui] = wi

    dist = warshall_floyd(graph)
    ans = 0

    for _ in range(n):
        si, ti = map(int, input().split())
        si -= 1
        ti -= 1
        ans += dist[si][ti]

    print(ans)


if __name__ == "__main__":
    main()
