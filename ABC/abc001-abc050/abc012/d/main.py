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
                if i == j:
                    dist[i][j] = 0
                    continue

                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    inf = float("inf")
    graph = [[inf for _ in range(n)] for _ in range(n)]

    for _ in range(m):
        ai, bi, ti = map(int, input().split())
        ai -= 1
        bi -= 1

        graph[ai][bi] = ti
        graph[bi][ai] = ti

    w = warshall_floyd(graph)

    ans = inf

    for wi in w:
        ans = min(ans, max(wi))

    print(ans)


if __name__ == "__main__":
    main()
