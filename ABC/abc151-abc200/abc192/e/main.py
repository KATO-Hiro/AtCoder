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

        for weight, edge, dep_time in edges[vertex]:
            new_cost = cost + ((dep_time - cost) % dep_time) + weight

            if new_cost < costs[edge]:
                costs[edge] = new_cost
                parents[edge] = vertex
                heappush(hq, (new_cost, edge))

    return costs


def main():
    import sys

    input = sys.stdin.readline

    n, m, x, y = map(int, input().split())
    edges = [[] for _ in range(n)]
    x -= 1
    y -= 1

    for _ in range(m):
        ai, bi, ti, ki = map(int, input().split())
        ai -= 1
        bi -= 1
        edges[ai].append((ti, bi, ki))
        edges[bi].append((ti, ai, ki))

    dist = dijkstra(vertex_count=n, source=x, edges=edges)
    ans = dist[y]

    if ans == float("inf"):
        ans = -1

    print(ans)


if __name__ == "__main__":
    main()
