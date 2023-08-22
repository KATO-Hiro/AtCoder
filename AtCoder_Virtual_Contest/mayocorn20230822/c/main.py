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
    parents = [[] for _ in range(vertex_count)]

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

                if new_cost < costs[edge]:
                    parents[edge] = [vertex]
                else:
                    parents[edge].append(vertex)

                heappush(hq, (new_cost, edge))

    return costs, parents


def main():
    import sys
    from collections import deque

    input = sys.stdin.readline

    n, m = map(int, input().split())
    edges = [[] for _ in range(n)]

    for _ in range(m):
        ai, bi = map(int, input().split())
        ai -= 1
        bi -= 1

        # ci: cost
        # bi: edge (0-indexed)
        ci = 1
        edges[ai].append((ci, bi))
        edges[bi].append((ci, ai))

    dist, parents = dijkstra(vertex_count=n, source=0, edges=edges)

    goal = n - 1
    q = deque([goal])
    visited = [False] * n
    dp = [0] * n
    dp[goal] = 1
    mod = 10**9 + 7

    while q:
        cur = q.popleft()

        if visited[cur]:
            continue

        visited[cur] = True

        for parent in parents[cur]:
            if visited[parent]:
                continue

            dp[parent] += dp[cur]
            dp[parent] %= mod

            q.append(parent)

    print(dp[0] % mod)


if __name__ == "__main__":
    main()
