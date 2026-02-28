# -*- coding: utf-8 -*-


def main():
    import sys

    sys.setrecursionlimit(10**8)

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    graph = [[] for _ in range(n)]

    for i, ai in enumerate(a):
        ai -= 1
        graph[i].append(ai)

    visited = [False] * n
    pending = -1
    ans = [pending] * n

    def dfs(cur, prev=-1):
        if visited[cur]:
            return

        visited[cur] = True

        for to in graph[cur]:
            if to == prev:
                continue

            dfs(to, cur)

            if cur == to:
                ans[cur] = cur + 1
            elif ans[to] != pending:
                ans[cur] = ans[to]

    for i in range(n):
        if visited[i]:
            continue

        dfs(i)

    print(*ans)


if __name__ == "__main__":
    main()
