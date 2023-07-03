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
    from collections import defaultdict

    input = sys.stdin.readline

    n, x, y = map(int, input().split())
    x -= 1
    y -= 1

    # 木 + サイクルが1箇所
    edges = [[] for _ in range(n)]
    ci = 1  # コスト

    for i in range(n - 1):
        edges[i].append((ci, i + 1))
        edges[i + 1].append((ci, i))

    edges[x].append((ci, y))
    edges[y].append((ci, x))

    ans = defaultdict(int)

    for i in range(n):
        dist, _ = dijkstra(vertex_count=n, source=i, edges=edges)

        for j in range(i + 1, n):
            ans[dist[j]] += 1
        # print(dist)

    for i in range(1, n):
        print(ans[i])


if __name__ == "__main__":
    main()
