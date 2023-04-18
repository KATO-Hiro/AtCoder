# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m, k = map(int, input().split())
    edges = [[] for _ in range(2 * n)]

    for _ in range(m):
        ai, bi, ci = map(int, input().split())
        ai -= 1
        bi -= 1

        # ci: cost
        # bi: edge (0-indexed)
        if ci == 0:
            edges[ai + n].append((1, bi + n))
            edges[bi + n].append((1, ai + n))
        else:
            edges[ai].append((1, bi))
            edges[bi].append((1, ai))

    s = list(map(int, input().split()))

    for si in s:
        si -= 1

        edges[si].append((0, si + n))
        edges[si + n].append((0, si))

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

        from collections import deque

        d = deque([(0, source)])
        costs = [float("inf") for _ in range(vertex_count)]
        costs[source] = 0
        visited = [False for _ in range(vertex_count)]
        pending = -1
        parents = [pending for _ in range(vertex_count)]

        while d:
            cost, vertex = d.popleft()

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

                    if weight == 0:
                        d.appendleft((new_cost, edge))
                    else:
                        d.append((new_cost, edge))

        return costs, parents

    dist, _ = dijkstra(vertex_count=2 * n, source=0, edges=edges)
    ans = min(dist[n - 1], dist[2 * n - 1])

    if ans == float('inf'):
        ans = -1

    print(ans)


if __name__ == "__main__":
    main()
