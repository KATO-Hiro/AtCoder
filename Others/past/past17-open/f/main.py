# -*- coding: utf-8 -*-


def main():
    import sys

    sys.setrecursionlimit(10**8)

    input = sys.stdin.readline

    n = int(input())
    p = list(map(int, input().split()))
    s = list(input().rstrip().split())
    mod = 998244353
    graph = [[] for _ in range(n)]

    for i, pi in enumerate(p, 1):
        pi -= 1
        graph[pi].append(i)

    def dfs(i):
        for g in graph[i]:
            dfs(g)

        if len(graph[i]) == 2:
            if s[i] == "+":
                s[i] = str((int(s[graph[i][0]]) + int(s[graph[i][1]])) % mod)
            else:
                s[i] = str((int(s[graph[i][0]]) * int(s[graph[i][1]])) % mod)

    dfs(0)
    print(int(s[0]))


if __name__ == "__main__":
    main()
