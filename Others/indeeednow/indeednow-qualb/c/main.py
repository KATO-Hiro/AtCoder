# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    graph = [[] for _ in range(n)]

    for _ in range(n - 1):
        ai, bi = map(int, input().split())
        ai -= 1
        bi -= 1

        graph[ai].append(bi)
        graph[bi].append(ai)

    from heapq import heappush, heappop

    hq = list()
    heappush(hq, 0)
    visited = [False for _ in range(n)]
    ans = list()

    while hq:
        vertex = heappop(hq)
        ans.append(vertex + 1)
        visited[vertex] = True

        for g in graph[vertex]:
            if visited[g]:
                continue

            heappush(hq, g)

    print(*ans)


if __name__ == "__main__":
    main()
