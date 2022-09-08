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

    a, b, x, y = map(int, input().split())
    a -= 1
    b -= 1
    b += 100

    edges = [[] for _ in range(201)]

    for i in range(100):
        # ci: cost
        # bi: edge (0-indexed)
        edges[i + 100].append((x, i))
        edges[i].append((x, i + 100))
        
        if i >= 1:
            edges[i + 99].append((x, i))
            edges[i].append((x, i + 99))

        if i < 99:
            edges[i].append((y, i + 1))
            edges[i + 1].append((y, i))

            edges[i + 100].append((y, i + 101))
            edges[i + 101].append((y, i + 100))

    dist, _ = dijkstra(vertex_count=200, source=a, edges=edges)
    print(dist[b])


if __name__ == "__main__":
    main()
