# -*- coding: utf-8 -*-

ans = list()


def main():
    import sys

    sys.setrecursionlimit(10**8)

    input = sys.stdin.readline

    n = int(input())
    graph = [[] for _ in range(n)]

    for _ in range(n - 1):
        ai, bi = map(int, input().split())
        ai -= 1
        bi -= 1

        graph[ai].append(bi)
        graph[bi].append(ai)

    def dfs(cur, parent=-1):
        global ans
        # print(cur)

        for to in sorted(graph[cur]):
            if to == parent:
                continue

            ans.append(cur + 1)
            # print("1", cur, to)
            dfs(to, cur)
            # print("2", cur, to)
            ans.append(to + 1)

        # print(cur)

    dfs(0)
    print(*ans, 1)


if __name__ == "__main__":
    main()
