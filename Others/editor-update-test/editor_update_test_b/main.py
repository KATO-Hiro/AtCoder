# -*- coding: utf-8 -*-


def main():
    import sys

    sys.setrecursionlimit(10**8)

    input = sys.stdin.readline

    n = int(input())
    graph = [[] for _ in range(n)]

    for i in range(1, n):
        pi = int(input())
        pi -= 1

        graph[i].append(pi)
        graph[pi].append(i)

    count = [0] * n

    def dfs(cur, parent=-1):
        for to in graph[cur]:
            if to == parent:
                continue

            dfs(to, cur)

            # print(cur, to)
            count[cur] += count[to]

        count[cur] += 1

    dfs(0)

    print(*count, sep="\n")


if __name__ == "__main__":
    main()
