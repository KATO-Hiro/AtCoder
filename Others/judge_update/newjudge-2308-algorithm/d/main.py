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

    n1, n2, m = map(int, input().split())
    edges1 = [[] for _ in range(n1)]
    edges2 = [[] for _ in range(n2)]

    for _ in range(m):
        ai, bi = map(int, input().split())
        ai -= 1
        bi -= 1

        # ci: cost
        # bi: edge (0-indexed)
        if ai < n1:
            edges1[ai].append((1, bi))
            edges1[bi].append((1, ai))
        else:
            ai -= n1
            bi -= n1
            edges2[ai].append((1, bi))
            edges2[bi].append((1, ai))

    dist1, _ = dijkstra(vertex_count=n1, source=0, edges=edges1)
    dist2, _ = dijkstra(vertex_count=n2, source=n2 - 1, edges=edges2)
    print(max(dist1) + max(dist2) + 1)


if __name__ == "__main__":
    main()
