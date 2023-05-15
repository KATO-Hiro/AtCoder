# -*- coding: utf-8 -*-


def main():
    import sys

    sys.setrecursionlimit(10**8)

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    graph = [[] for _ in range(n + 1)]

    for i, ai in enumerate(a, 1):
        ai -= 1
        graph[ai].append(i)
        graph[i].append(ai)

    ans = [0] * n

    def dfs(i, parent=-1):
        for to in graph[i]:
            if to == parent:
                continue

            ans[i] += 1
            dfs(to, i)

    dfs(0)

    for ans_i in ans:
        print(ans_i)


if __name__ == "__main__":
    main()
