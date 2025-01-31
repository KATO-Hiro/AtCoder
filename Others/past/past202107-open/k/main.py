# -*- coding: utf-8 -*-


def main():
    import sys
    from heapq import heappop, heappush

    input = sys.stdin.readline

    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    graph = [[] for _ in range(n)]

    for _ in range(m):
        ui, vi, ti = map(int, input().split())
        ui -= 1
        vi -= 1

        graph[ui].append((ti, vi))
        graph[vi].append((ti, ui))

    hq = [(0, 0)]  # weight, vertex number (0-indexed)
    inf = 10**18
    costs = [inf] * n
    costs[0] = 0
    values = [0] * n
    values[0] = a[0]

    while hq:
        cost, vertex = heappop(hq)

        if cost > costs[vertex]:
            continue

        for weight, edge in graph[vertex]:
            new_cost = cost + weight
            new_value = values[vertex] + a[edge]

            # See:
            # https://atcoder.jp/contests/past202107-open/submissions/24435383
            if new_cost > costs[edge]:
                continue
            if new_cost == costs[edge] and new_value <= values[edge]:
                continue

            costs[edge] = new_cost
            values[edge] = new_value
            heappush(hq, (new_cost, edge))

    print(values[-1])


if __name__ == "__main__":
    main()
