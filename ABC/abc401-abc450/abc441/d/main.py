# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict
    from itertools import pairwise

    sys.setrecursionlimit(10**8)

    input = sys.stdin.readline

    n, m, l, s, t = map(int, input().split())
    costs = defaultdict(int)
    graph = [[] for _ in range(n)]

    for i in range(m):
        ai, bi, ci = map(int, input().split())
        ai -= 1
        bi -= 1

        graph[ai].append((bi, i))
        costs[(ai, bi, i)] = ci

    paths = [(0, 0)]
    ans = set()

    def dfs(cur, prev=-1):
        if len(paths) == l + 1:
            total = 0

            for (ui, i), (vj, j) in pairwise(paths):
                total += costs[(ui, vj, j)]

            if s <= total <= t:
                ans.add(paths[-1][0] + 1)

            return

        for to, j in graph[cur]:
            paths.append((to, j))
            dfs(to, cur)
            paths.pop()

    dfs(0)
    ans = sorted(ans)
    print(*ans)


if __name__ == "__main__":
    main()
