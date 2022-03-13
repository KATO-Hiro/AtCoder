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
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    edges = list()
    inf = 10 ** 18
    graph = [[inf] * n for _ in range(n)]
    
    for _ in range(m):
        ai, bi, ci = map(int, input().split())
        ai -= 1
        bi -= 1
    
        edges.append([ai, bi, ci])
        graph[ai][bi] = ci
        graph[bi][ai] = ci
    
    dist = warshall_floyd(graph)
    ans = 0

    for ai, bi, ci in edges:
        for i in range(n):
            if dist[ai][i] + dist[i][bi] <= ci:
                ans += 1
                break

    print(ans)


if __name__ == "__main__":
    main()
