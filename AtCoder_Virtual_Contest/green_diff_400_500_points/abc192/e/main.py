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

        for weight, ki, edge in edges[vertex]:
            waiting = (ki - (cost % ki)) % ki
            new_cost = cost + waiting + weight

            if new_cost < costs[edge]:
                costs[edge] = new_cost
                parents[edge] = vertex
                heappush(hq, (new_cost, edge))

    return costs, parents


def main():
    import sys

    input = sys.stdin.readline

    n, m, x, y = map(int, input().split())
    x -= 1
    y -= 1
    edges = [[] for _ in range(n)]

    for _ in range(m):
        ai, bi, ti, ki = map(int, input().split())
        ai -= 1
        bi -= 1

        # ti: cost
        # bi: edge (0-indexed)
        edges[ai].append((ti, ki, bi))
        edges[bi].append((ti, ki, ai))

    dist, _ = dijkstra(vertex_count=n, source=x, edges=edges)
    ans = dist[y]

    if ans == float("inf"):
        ans = -1

    print(ans)


if __name__ == "__main__":
    main()
