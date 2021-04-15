# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline
    sys.setrecursionlimit(10 ** 7)

    n = int(input())
    c = list(map(int, input().split()))
    graph = [[] for _ in range(10 ** 5 + 1)]

    for _ in range(n - 1):
        ai, bi = map(int, input().split())
        ai -= 1
        bi -= 1

        graph[ai].append(bi)
        graph[bi].append(ai)

    good = [False for _ in range(10 ** 5 + 1)]
    count = [0 for _ in range(10 ** 5 + 1)]

    def dfs(current_v, parent=-1):
        if count[c[current_v]] == 0:
            good[current_v] = True

        count[c[current_v]] += 1

        for g in graph[current_v]:
            if g != parent:
                dfs(g, current_v)

        count[c[current_v]] -= 1

    dfs(0)

    for i in range(n):
        if good[i]:
            print(i + 1)


if __name__ == "__main__":
    main()
