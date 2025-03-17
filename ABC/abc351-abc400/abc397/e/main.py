# -*- coding: utf-8 -*-

ok = True


def main():
    import sys

    sys.setrecursionlimit(10**8)

    input = sys.stdin.readline

    n, k = map(int, input().split())
    nk = n * k
    graph = [[] for _ in range(nk)]

    for _ in range(nk - 1):
        ai, bi = map(int, input().split())
        ai -= 1
        bi -= 1

        graph[ai].append(bi)
        graph[bi].append(ai)

    def dfs(cur, parent=-1):
        global ok

        size_total = 1
        degree = 0

        for child in graph[cur]:
            if child == parent:
                continue

            size = dfs(child, cur)

            if size % k != 0:
                degree += 1

            size_total += size

        if size_total % k != 0:
            degree += 1
        if degree >= 3:
            ok = False

        return size_total

    dfs(0)

    if ok:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
