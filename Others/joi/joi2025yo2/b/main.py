# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import deque

    input = sys.stdin.readline

    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    p = list(map(int, input().split()))
    inf = 10**18
    dist = [inf] * n
    graph = [[] for _ in range(n)]
    q = deque()
    visited = [False] * n

    for i, (ai, pi) in enumerate(zip(a, p)):
        if pi == -1:
            dist[i] = ai
            q.append(i)
        else:
            pi -= 1
            graph[pi].append(i)

    while q:
        cur = q.popleft()

        if visited[cur]:
            continue

        visited[cur] = True

        for to in graph[cur]:
            if visited[to]:
                continue

            dist[to] = min(dist[to], dist[cur] + a[to])
            q.append(to)

    ans = -1

    for i, di in enumerate(dist, 1):
        if di > x:
            continue

        ans = max(ans, i)

    print(ans)


if __name__ == "__main__":
    main()
