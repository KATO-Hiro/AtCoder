# -*- coding: utf-8 -*-


def dijkstra(vertex_count: int, source: int, edges):
    """Uses Dijkstra's algorithm to find the shortest path in a graph.

    Args:
        vertex_count: The number of vertices.
        source      : Vertex number (0-indexed).
        edges       : List of (cost, edge) (0-indexed).

    Returns:
        costs  : List of the shortest distance.
        parents: List of parent vertices.

    Landau notation: O(|Edges|log|Vertices|).

    See:
    https://atcoder.jp/contests/abc191/submissions/19964078
    https://atcoder.jp/contests/abc191/submissions/19966232
    """

    from heapq import heappop, heappush

    hq = [(0, source)]  # weight, vertex number (0-indexed)
    costs = [float("inf") for _ in range(vertex_count)]
    costs[source] = 0
    visited = [False for _ in range(vertex_count)]
    pending = -1
    parents = [pending for _ in range(vertex_count)]

    while hq:
        cost, vertex = heappop(hq)

        if cost > costs[vertex]:
            continue

        if visited[vertex]:
            continue

        visited[vertex] = True

        for weight, edge in edges[vertex]:
            new_cost = cost + weight

            if new_cost < costs[edge]:
                costs[edge] = new_cost
                parents[edge] = vertex
                heappush(hq, (new_cost, edge))

    return costs, parents


def main():
    import sys
    from collections import deque

    input = sys.stdin.readline

    n, s, t = map(int, input().split())
    s -= 1
    t -= 1

    graph = [[] for _ in range(n)]

    for _ in range(n - 1):
        ai, bi = map(int, input().split())
        ai -= 1
        bi -= 1

        graph[ai].append((1, bi))
        graph[bi].append((1, ai))

    costs, parents = dijkstra(n, s, graph)
    # print(costs, parents)
    pos = t
    paths = list()

    while pos != -1:
        paths.append(pos)
        pos = parents[pos]

    # print(paths[::-1])

    inf = 10**18
    d = deque(paths[::-1])
    # print(d)
    visited = [False] * n
    dist = [inf] * n

    for node in paths:
        dist[node] = 1

    # print(dist)

    while d:
        cur = d.pop()

        if visited[cur]:
            continue

        visited[cur] = True

        for _, to in graph[cur]:
            if visited[to]:
                continue

            d.append(to)
            dist[to] = min(dist[to], dist[cur] + 1)

    print(*dist, sep="\n")


if __name__ == "__main__":
    main()
