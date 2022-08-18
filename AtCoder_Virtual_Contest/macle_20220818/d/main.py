# -*- coding: utf-8 -*-


def warshall_floyd(dist):
    '''
        Args:
            Distance matrix between two points.
        Returns:
            Matrix of shortest distance.
        Landau notation: O(n ** 3).
    '''

    v_count = len(dist[0])

    for k in range(v_count):
        for i in range(v_count):
            for j in range(v_count):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist


def main():
    from copy import deepcopy
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    inf = 10 ** 6
    graph = [[inf for _ in range(n)] for _ in range(n)]
    
    for _ in range(m):
        ai, bi, ci = map(int, input().split())
        ai -= 1
        bi -= 1
    
        graph[ai][bi] = ci
        graph[bi][ai] = ci

    g = deepcopy(graph)
    dist = warshall_floyd(g)
    ans = 0

    for i in range(n):
        for j in range(i + 1, n):
            if graph[i][j] == inf:
                continue

            if graph[i][j] != dist[i][j]:
                ans += 1

    print(ans)


if __name__ == "__main__":
    main()
