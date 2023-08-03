# -*- coding: utf-8 -*-


def main():
    import sys

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

    colors = [0] * (10**5 + 1)
    ans = []

    def dfs(cur, parent=-1):
        if colors[c[cur]] == 0:
            ans.append(cur + 1)

        colors[c[cur]] += 1

        for to in graph[cur]:
            if to == parent:
                continue

            dfs(to, cur)

        # 元に戻す
        colors[c[cur]] -= 1

    dfs(0)
    print(*sorted(ans), sep="\n")


if __name__ == "__main__":
    main()
