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

    n, m, k = map(int, input().split())
    graph = [[] for _ in range(n)]

    for _ in range(m):
        ai, bi, cost = map(int, input().split())
        ai -= 1
        bi -= 1

        graph[ai].append((cost, bi))
        graph[bi].append((cost, ai))

    events = [(0, 0)]  # 時刻0で頂点0にいる

    for _ in range(k):
        ci, ti = map(int, input().split())
        ci -= 1
        events.append((ti, ci))

    events.sort()
    inf = 10**9
    dp = [-inf] * (k + 1)
    dp[0] = 0

    for i, (ti, ci) in enumerate(events):
        dists, _ = dijkstra(vertex_count=n, source=ci, edges=graph)

        for j in range(i + 1, k + 1):
            tj, cj = events[j]

            if ti + dists[cj] <= tj:
                dp[j] = max(dp[j], dp[i] + 1)

    print(max(dp))


if __name__ == "__main__":
    main()
