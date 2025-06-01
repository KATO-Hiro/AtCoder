# -*- coding: utf-8 -*-


def dijkstra(vertex_count: int, source: int, edges, wj):
    from heapq import heappop, heappush

    hq = [(0, source)]  # weight, vertex number (0-indexed)
    costs = [float("inf") for _ in range(vertex_count)]
    costs[source] = 0
    visited = [False for _ in range(vertex_count)]

    while hq:
        cost, vertex = heappop(hq)

        if cost > costs[vertex]:
            continue

        if visited[vertex]:
            continue

        visited[vertex] = True

        for weight, edge in edges[vertex]:
            new_cost = cost | weight

            if weight & wj == weight and new_cost < costs[edge]:
                costs[edge] = new_cost
                heappush(hq, (new_cost, edge))

    return costs[-1] < float("inf")


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]

    for _ in range(m):
        ai, bi, ci = map(int, input().split())
        ai -= 1
        bi -= 1
        graph[ai].append((ci, bi))
        graph[bi].append((ci, ai))

    ng, ok = -1, 2**30 - 1

    while abs(ok - ng) > 1:
        wj = (ok + ng) // 2
        result = dijkstra(vertex_count=n, source=0, edges=graph, wj=wj)

        if result:
            ok = wj
        else:
            ng = wj

    print(ok)


if __name__ == "__main__":
    main()
