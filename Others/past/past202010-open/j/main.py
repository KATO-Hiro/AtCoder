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

    n, m = map(int, input().split())
    v = n + 6
    graph = [[] for _ in range(v)]
    xab, xac, xbc = list(map(int, input().split()))
    s = input().rstrip()

    for i, si in enumerate(s):
        if si == "A":
            graph[i].append((0, n))  # i → Ain
            graph[n + 1].append((0, i))  # Aout → i

            graph[n].append((xab, n + 3))  # Ain → Bout
            graph[n].append((xac, n + 5))  # Ain → Cout
        elif si == "B":
            graph[i].append((0, n + 2))  # i → Bin
            graph[n + 3].append((0, i))  # Bout → i

            graph[n + 2].append((xab, n + 1))  # Bin → Aout
            graph[n + 2].append((xbc, n + 5))  # Bin → Cout
        elif si == "C":
            graph[i].append((0, n + 4))  # i → Cin
            graph[n + 5].append((0, i))  # Cout → i

            graph[n + 4].append((xac, n + 1))  # Cin → Aout
            graph[n + 4].append((xbc, n + 3))  # Cin → Bout

    for _ in range(m):
        ai, bi, ci = map(int, input().split())
        ai -= 1
        bi -= 1

        graph[ai].append((ci, bi))
        graph[bi].append((ci, ai))

    dist, _ = dijkstra(vertex_count=v, source=0, edges=graph)
    ans = dist[n - 1]
    print(ans)


if __name__ == "__main__":
    main()
