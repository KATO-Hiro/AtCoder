# -*- coding: utf-8 -*-


def solve():
    n, m, x, y = map(int, input().split())
    x -= 1
    y -= 1

    graph = [[] for _ in range(n)]

    for _ in range(m):
        ai, bi = map(int, input().split())
        ai -= 1
        bi -= 1

        graph[ai].append(bi)
        graph[bi].append(ai)

    for g in graph:
        g.sort()

    visited = [False] * n
    ans = []

    def dfs(cur, parent=-1):
        ans.append(cur + 1)

        if cur == y:
            return True

        visited[cur] = True

        for to in graph[cur]:
            if to == parent:
                continue
            if visited[to]:
                continue

            if dfs(to, cur):
                return True

        ans.pop()

        return False

    dfs(x)
    print(*ans)


def main():
    import sys

    sys.setrecursionlimit(10**6)

    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
