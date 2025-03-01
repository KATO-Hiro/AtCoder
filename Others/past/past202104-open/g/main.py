# -*- coding: utf-8 -*-


def main():
    import sys
    from heapq import heappop, heappush

    input = sys.stdin.readline

    n, m, q = map(int, input().split())
    graph = [[] for _ in range(n)]

    for _ in range(m):
        ai, bi, ci = map(int, input().split())
        ai -= 1
        bi -= 1

        graph[ai].append((ci, bi))
        graph[bi].append((ci, ai))

    x = list(map(int, input().split()))

    hq = []
    visited = [False] * n
    visited[0] = True
    count = 1

    for cost, to in graph[0]:
        heappush(hq, (cost, to))

    for xi in x:
        candidates = set()

        while hq:
            ci, cur = heappop(hq)

            if ci > xi:
                heappush(hq, (ci, cur))
                break

            if visited[cur]:
                continue

            visited[cur] = True
            count += 1

            for cost, to in graph[cur]:
                candidates.add((cost, to))

        for candidate in candidates:
            heappush(hq, candidate)

        print(count)


if __name__ == "__main__":
    main()
