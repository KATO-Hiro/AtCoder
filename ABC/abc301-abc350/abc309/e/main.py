# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import deque

    input = sys.stdin.readline

    n, m = map(int, input().split())
    p = list(map(int, input().split()))
    graph = [[] for _ in range(n)]

    for i, pi in enumerate(p, 1):
        pi -= 1
        graph[pi].append(i)

    count = [-1] * n

    for _ in range(m):
        xi, yi = map(int, input().split())
        xi -= 1
        count[xi] = max(count[xi], yi)

    d = deque([0])
    visited = [False] * n

    while d:
        cur = d.popleft()

        if visited[cur]:
            continue

        visited[cur] = True

        for to in graph[cur]:
            if visited[to]:
                continue

            count[to] = max(count[to], count[cur] - 1)

            d.append(to)

    print(sum([1 for ci in count if ci >= 0]))


if __name__ == "__main__":
    main()
