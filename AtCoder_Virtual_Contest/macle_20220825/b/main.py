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

    n, m = map(int, input().split())
    edges = [[] for _ in range(n)]

    for _ in range(m):
        ai, bi = map(int, input().split())
        ai -= 1
        bi -= 1

        # ci: cost
        # xi: edge (0-indexed)
        # yi: edge (0-indexed)
        edges[ai].append((1, bi))
        edges[bi].append((1, ai))

    path_count = dijkstra(vertex_count=n, source=0, edges=edges)

    print(path_count[n - 1])


if __name__ == "__main__":
    main()
