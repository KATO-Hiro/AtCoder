# -*- coding: utf-8 -*-


def main():
    import sys

    sys.setrecursionlimit(10**8)

    input = sys.stdin.readline

    n = int(input())
    x = list(map(int, input().split()))
    graph = [[] for _ in range(n)]

    for _ in range(n - 1):
        ai, bi, ci = map(int, input().split())
        ai -= 1
        bi -= 1

        graph[ai].append((ci, bi))
        graph[bi].append((ci, ai))

    ans = 0

    def dfs(cur, parent=-1):
        nonlocal ans

        for cost, to in graph[cur]:
            if to == parent:
                continue

            dfs(to, cur)
            x[cur] += x[to]
            ans += abs(x[to]) * cost

    dfs(0)
    print(ans)


if __name__ == "__main__":
    main()
