# -*- coding: utf-8 -*-


def main():
    import sys

    sys.setrecursionlimit(10**8)

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))

    graph = [[] for _ in range(n)]

    for i, ai in enumerate(a, 1):
        ai -= 1

        graph[i].append(ai)
        graph[ai].append(i)

    visited = [False] * n
    ans = [0] * n

    def dfs(cur, parent=-1):
        if visited[cur]:
            return

        visited[cur] = True

        for to in graph[cur]:
            if visited[to]:
                continue

            if to == parent:
                continue

            dfs(to, cur)
            ans[cur] += ans[to] + 1

    dfs(0)
    print(*ans)


if __name__ == "__main__":
    main()
