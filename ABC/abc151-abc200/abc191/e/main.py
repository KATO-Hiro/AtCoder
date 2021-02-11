# -*- coding: utf-8 -*-


def dijkstra(vertex_count: int, source: int, edges):
    from heapq import heappop, heappush

    hq = [(0, source)]  # weight, vertex number (0-indexed)
    costs = [float("inf") for _ in range(vertex_count)]
    costs[source] = 0
    pending = -1
    parents = [pending for _ in range(vertex_count)]

    while hq:
        cost, vertex = heappop(hq)

        if cost > costs[vertex]:
            continue

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
    edges = [[] for _ in range(n)]
    reversed_edges = [[] for _ in range(n)]

    for _ in range(m):
        ai, bi, ci = map(int, input().split())
        ai -= 1
        bi -= 1

        edges[ai].append((ci, bi))
        reversed_edges[bi].append((ci, ai))

    for i in range(n):
        dist, _ = dijkstra(vertex_count=n, source=i, edges=edges)
        ans = float("inf")

        for cost, reversed_edge in reversed_edges[i]:
            ans = min(ans, dist[reversed_edge] + cost)

        if ans == float("inf"):
            print(-1)
        else:
            print(ans)


if __name__ == "__main__":
    main()
