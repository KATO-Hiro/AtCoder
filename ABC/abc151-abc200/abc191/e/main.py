# -*- coding: utf-8 -*-


def dijkstra(vertex_count: int, source: int, edges):
    from heapq import heappop, heappush

    hq = [(0, source)]  # weight, vertex number (0-indexed)
    costs = [float("inf") for _ in range(vertex_count)]
    costs[source] = 0
    pending = -1
    parents = [pending for _ in range(vertex_count)]
    ans = float("inf")

    while hq:
        cost, vertex = heappop(hq)

        if cost > costs[vertex]:
            continue

        for weight, edge in edges[vertex]:
            new_cost = cost + weight

            if edge == source:
                ans = min(ans, new_cost)

            if new_cost < costs[edge]:
                costs[edge] = new_cost
                parents[edge] = vertex
                heappush(hq, (new_cost, edge))

    return ans


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    edges = [[] for _ in range(n)]

    for _ in range(m):
        ai, bi, ci = map(int, input().split())
        ai -= 1
        bi -= 1

        edges[ai].append((ci, bi))

    for i in range(n):
        dist = dijkstra(vertex_count=n, source=i, edges=edges)

        if dist == float("inf"):
            print(-1)
        else:
            print(dist)


if __name__ == "__main__":
    main()
