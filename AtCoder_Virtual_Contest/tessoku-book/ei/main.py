# -*- coding: utf-8 -*-


def main():
    import sys

    sys.setrecursionlimit(10**7)

    input = sys.stdin.readline

    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]

    for _ in range(m):
        ai, bi = map(int, input().split())
        ai -= 1
        bi -= 1

        graph[ai].append(bi)
        graph[bi].append(ai)

    prev = [-1] * n
    visited = [False] * n

    def dfs(cur, parent=-1):
        if visited[cur]:
            return

        visited[cur] = True

        for to in graph[cur]:
            if to == parent:
                continue
            if visited[to]:
                continue

            if prev[to] == -1:
                prev[to] = cur

            dfs(to, cur)

    dfs(0)

    pos = n - 1
    ans = list()

    while pos != -1:
        ans.append(pos + 1)
        pos = prev[pos]

    print(*ans[::-1])


if __name__ == "__main__":
    main()
