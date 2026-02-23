# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import deque

    input = sys.stdin.readline

    n, q = map(int, input().split())
    v = list(map(int, input().split()))
    p = list(map(int, input().split()))
    graph = [[] for _ in range(n)]

    for i, pi in enumerate(p, 1):
        pi -= 1

        graph[i].append(pi)
        graph[pi].append(i)

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

            v[to] += v[cur]
            d.append(to)

    ans = []

    for _ in range(q):
        xi = int(input())
        xi -= 1
        ans.append(v[xi])

    print(*ans, sep="\n")


if __name__ == "__main__":
    main()
