# -*- coding: utf-8 -*-


def main():
    import sys

    sys.setrecursionlimit(10**8)

    input = sys.stdin.readline

    n, t = map(int, input().split())
    t -= 1
    graph = [[] for _ in range(n)]

    for _ in range(n - 1):
        ai, bi = map(int, input().split())
        ai -= 1
        bi -= 1

        graph[ai].append(bi)
        graph[bi].append(ai)

    ans = [0] * n

    def dfs(cur, parent=-1):
        for to in graph[cur]:
            if to == parent:
                continue

            dfs(to, cur)
            ans[cur] = max(ans[cur], ans[to] + 1)

    dfs(t)
    print(*ans)


if __name__ == "__main__":
    main()
