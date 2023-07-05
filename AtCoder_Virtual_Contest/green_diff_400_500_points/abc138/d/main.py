# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import deque

    input = sys.stdin.readline

    n, q = map(int, input().split())
    dp = [0] * n
    graph = [[] for _ in range(n)]

    for _ in range(n - 1):
        ai, bi = map(int, input().split())
        ai -= 1
        bi -= 1

        graph[ai].append(bi)
        graph[bi].append(ai)

    for _ in range(q):
        pi, xi = map(int, input().split())
        pi -= 1
        dp[pi] += xi

    q = deque([0])
    visited = [False] * n

    while q:
        cur = q.popleft()

        if visited[cur]:
            continue

        visited[cur] = True

        for to in graph[cur]:
            if visited[to]:
                continue

            dp[to] += dp[cur]
            q.append(to)

    print(*dp)


if __name__ == "__main__":
    main()
