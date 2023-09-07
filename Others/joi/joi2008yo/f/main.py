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

    input = sys.stdin.readline

    n, k = map(int, input().split())
    graph = [[] for _ in range(n)]
    used = set()

    for _ in range(k):
        qi, *values = map(int, input().split())

        if qi == 0:
            ai, bi = values
            ai -= 1
            bi -= 1

            dist, _ = dijkstra(vertex_count=n, source=ai, edges=graph)

            ans = dist[bi]

            if ans == float("inf"):
                ans = -1

            print(ans)
        else:
            ci, di, ei = values
            ci -= 1
            di -= 1

            if (ci, di) in used or (di, ci) in used:
                continue

            graph[ci].append((ei, di))
            graph[di].append((ei, ci))


if __name__ == "__main__":
    main()
