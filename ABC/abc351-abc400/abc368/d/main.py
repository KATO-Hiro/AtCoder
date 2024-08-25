# -*- coding: utf-8 -*-


def main():
    import sys

    sys.setrecursionlimit(10**8)

    input = sys.stdin.readline

    n, k = map(int, input().split())
    graph = [[] for _ in range(n)]

    for _ in range(n - 1):
        ai, bi = map(int, input().split())
        ai -= 1
        bi -= 1

        graph[ai].append(bi)
        graph[bi].append(ai)

    v = list(map(lambda x: int(x) - 1, input().split()))
    sv = set(v)
    needed = [i in sv for i in range(n)]

    def dfs(cur, parent=-1):
        for to in graph[cur]:
            if to == parent:
                continue

            # print("in: ", cur, to)
            dfs(to, cur)
            # print("out: ", cur, to)

            if needed[to]:
                needed[cur] = True

    dfs(v[0])

    print(sum(needed))


if __name__ == "__main__":
    main()
