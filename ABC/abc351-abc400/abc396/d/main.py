# -*- coding: utf-8 -*-

inf = 10**20
ans = inf


def main():
    import sys

    sys.setrecursionlimit(10**8)

    input = sys.stdin.readline

    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]

    for _ in range(m):
        ai, bi, wi = map(int, input().split())
        ai -= 1
        bi -= 1
        graph[ai].append((wi, bi))
        graph[bi].append((wi, ai))

    visited = [False] * n

    def dfs(cur, xor_total):
        global ans
        visited[cur] = True

        if cur == n - 1:
            ans = min(ans, xor_total)

        for wi, to in graph[cur]:
            if visited[to]:
                continue

            dfs(to, xor_total ^ wi)

        visited[cur] = False

    dfs(0, 0)
    print(ans)


if __name__ == "__main__":
    main()
