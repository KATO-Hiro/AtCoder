# -*- coding: utf-8 -*-

from heapq import heappush, heappop


def solve():
    n, m, x, y = map(int, input().split())
    x -= 1
    y -= 1

    graph = [[] for _ in range(n)]

    for _ in range(m):
        ai, bi = map(int, input().split())
        ai -= 1
        bi -= 1

        graph[ai].append(bi)
        graph[bi].append(ai)

    hq = []
    heappush(hq, [x])
    visited = [False] * n

    while hq:
        path = heappop(hq)
        cur = path[-1]

        if cur == y:
            print(*[i + 1 for i in path])

            return

        if visited[cur]:
            continue

        visited[cur] = True

        for to in sorted(graph[cur]):
            if visited[to]:
                continue

            heappush(hq, path + [to])


def main():
    import sys

    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
