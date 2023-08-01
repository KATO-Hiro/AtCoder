# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict, deque

    input = sys.stdin.readline

    n, q = map(int, input().split())
    graph = [[] for _ in range(n)]

    for _ in range(n - 1):
        ai, bi = map(int, input().split())
        ai -= 1
        bi -= 1

        graph[ai].append(bi)
        graph[bi].append(ai)

    d = defaultdict(int)

    for _ in range(q):
        pi, xi = map(int, input().split())
        pi -= 1
        d[pi] += xi

    que = deque()
    que.append(0)
    visited = [False] * n
    ans = [0] * n
    ans[0] = d[0]  # Initialize

    while que:
        cur = que.popleft()

        if visited[cur]:
            continue

        visited[cur] = True

        for to in graph[cur]:
            if visited[to]:
                continue

            ans[to] += ans[cur] + d[to]
            que.append(to)

    print(*ans)


if __name__ == "__main__":
    main()
