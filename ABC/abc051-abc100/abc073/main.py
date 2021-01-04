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
    from itertools import permutations
    import sys

    input = sys.stdin.readline

    n, m, _ = map(int, input().split())
    r = list(map(lambda x: int(x) - 1, input().split()))
    INF = 10 ** 12
    dist = [[INF for _ in range(n)] for _ in range(n)]

    for i in range(m):
        ai, bi, ci = map(int, input().split())
        ai -= 1
        bi -= 1

        dist[ai][bi] = ci
        dist[bi][ai] = ci

    dist_min = warshall_floyd(dist)
    ans = float("inf")

    patterns = permutations(r)

    for pattern in patterns:
        cost = 0

        for first, second in zip(pattern, pattern[1:]):
            cost += dist_min[first][second]

        ans = min(ans, cost)

    print(ans)


if __name__ == "__main__":
    main()
