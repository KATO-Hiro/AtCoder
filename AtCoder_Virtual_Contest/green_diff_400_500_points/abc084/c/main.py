# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    edges = [[] for _ in range(n)]
    s, f = [0] * n, [0] * n

    for i in range(n - 1):
        ci, si, fi = map(int, input().split())

        edges[i].append((ci, i + 1))
        s[i], f[i] = si, fi

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
                new_cost = max(cost, s[vertex])
                fi = f[vertex]

                extra_cost = (fi - (new_cost % fi)) % fi
                new_cost += extra_cost
                new_cost += weight
                # print(vertex, edge, new_cost, extra_cost, new_cost)

                if new_cost < costs[edge]:
                    costs[edge] = new_cost
                    parents[edge] = vertex
                    heappush(hq, (new_cost, edge))

        return costs, parents

    for i in range(n):
        dist, _ = dijkstra(vertex_count=n, source=i, edges=edges)
        print(dist[-1])


if __name__ == "__main__":
    main()
