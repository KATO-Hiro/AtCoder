# -*- coding: utf-8 -*-


from collections import deque


def bfs(vertex_count, source, graph):
    inf = float("inf")
    costs = [inf for _ in range(vertex_count)]
    costs[source] = 0
    visited = [False for _ in range(vertex_count)]
    q = deque([source])

    while q:
        cur = q.popleft()

        if visited[cur]:
            continue

        visited[cur] = True

        for to in graph[cur]:
            if visited[to]:
                continue

            costs[to] = min(costs[to], costs[cur] + 1)
            q.append(to)
    
    return costs


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    edges = [[] for _ in range(n)]

    for _ in range(m):
        ai, bi = map(int, input().split())
        ai -= 1
        bi -= 1
        edges[ai].append(bi)
    
    inf = float('inf')
    ans = 0

    for i in range(n):
        dist = bfs(n, i, edges)

        for di in dist:
            if di == 0 or di == 1 or di == inf:
                continue

            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
