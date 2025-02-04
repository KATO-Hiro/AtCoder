# -*- coding: utf-8 -*-

inf = 10**18


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
    costs = [inf for _ in range(vertex_count)]
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

    input = sys.stdin.readline

    n, m = map(int, input().split())
    graph1 = [[] for _ in range(n)]
    graph2 = [[] for _ in range(n)]

    for _ in range(m):
        ui, vi, wi = map(int, input().split())
        ui -= 1
        vi -= 1

        graph1[ui].append((wi, vi))
        graph2[vi].append((wi, ui))

    dist1, _ = dijkstra(vertex_count=n, source=0, edges=graph1)
    dist2, _ = dijkstra(vertex_count=n, source=n - 1, edges=graph2)

    for d1, d2 in zip(dist1, dist2):
        if d1 == inf or d2 == inf:
            ans = -1
        else:
            ans = d1 + d2

        print(ans)


if __name__ == "__main__":
    main()
