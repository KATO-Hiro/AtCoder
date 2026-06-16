# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import deque

    input = sys.stdin.readline

    n, m, k = map(int, input().split())
    s = list(map(lambda x: int(x) - 1, input().split()))
    graph = [[] for _ in range(n)]

    for _ in range(m):
        ai, bi = map(int, input().split())
        ai -= 1
        bi -= 1

        graph[ai].append(bi)
        graph[bi].append(ai)

    q = deque(s)
    visited = [False] * n

    while q:
        cur = q.popleft()

        if visited[cur]:
            continue

        visited[cur] = True

        for to in graph[cur]:
            if visited[to]:
                continue

            q.append(to)

    ans = sum(visited)
    print(ans)


if __name__ == "__main__":
    main()
