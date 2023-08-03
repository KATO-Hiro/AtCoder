# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict

    sys.setrecursionlimit(10**8)

    input = sys.stdin.readline

    n = int(input())
    c = list(map(int, input().split()))
    graph = [[] for _ in range(n)]

    for _ in range(n - 1):
        ai, bi = map(int, input().split())
        ai -= 1
        bi -= 1

        graph[ai].append(bi)
        graph[bi].append(ai)

    visited = [False] * n
    d = defaultdict(set)
    d[c[0]].add(0)
    ans = [1]

    def dfs(cur, parent=-1):
        visited[cur] = True

        for to in graph[cur]:
            if visited[to]:
                continue

            if to == parent:
                continue

            # print("from: ", cur, to)

            if len(d[c[to]]) == 0:
                ans.append(to + 1)

            d[c[to]].add(to)
            # print(c[to], d[c[to]])
            dfs(to, cur)
            # print("to: ", cur, to)
            d[c[to]].remove(to)
            # print(c[to], d[c[to]])

    dfs(0)
    print(*sorted(ans), sep="\n")


if __name__ == "__main__":
    main()
