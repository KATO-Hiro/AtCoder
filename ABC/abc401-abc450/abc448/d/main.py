# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict

    input = sys.stdin.readline
    sys.setrecursionlimit(10**8)

    n = int(input())
    a = list(map(int, input().split()))
    graph = [[] for _ in range(n)]

    for _ in range(n - 1):
        ai, bi = map(int, input().split())
        ai -= 1
        bi -= 1

        graph[ai].append(bi)
        graph[bi].append(ai)

    d = defaultdict(int)
    d[a[0]] += 1
    ans = ["No"] * n

    def dfs(cur, prev=-1):
        for to in graph[cur]:
            if to == prev:
                continue

            d[a[to]] += 1

            if d[a[to]] >= 2 or ans[cur] == "Yes":
                ans[to] = "Yes"

            dfs(to, cur)
            d[a[to]] -= 1

    dfs(0)
    print(*ans, sep="\n")


if __name__ == "__main__":
    main()
