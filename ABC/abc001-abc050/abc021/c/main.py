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
    path_count = [0 for _ in range(vertex_count)]
    path_count[source] = 1
    mod = 10 ** 9 + 7

    while hq:
        cost, vertex = heappop(hq)

        if cost > costs[vertex]:
            continue

        if visited[vertex]:
            continue

        visited[vertex] = True

        for weight, edge in edges[vertex]:
            new_cost = cost + weight

            if new_cost <= costs[edge]:
                costs[edge] = new_cost

                path_count[edge] += path_count[vertex]
                path_count[edge] %= mod

                heappush(hq, (new_cost, edge))

    return path_count


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    m = int(input())
    edges = [[] for _ in range(n)]

    for _ in range(m):
        xi, yi = map(int, input().split())
        xi -= 1
        yi -= 1
        # ci: cost
        # xi: edge (0-indexed)
        # yi: edge (0-indexed)
        edges[xi].append((1, yi))
        edges[yi].append((1, xi))

    path_counts = dijkstra(vertex_count=n, source=a, edges=edges)

    print(path_counts[b])


if __name__ == "__main__":
    main()
