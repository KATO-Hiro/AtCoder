# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]

    for _ in range(m):
        ai, bi = map(int, input().split())
        ai -= 1
        bi -= 1

        graph[ai].append(bi)
        graph[bi].append(ai)

    ans = []

    for g in graph:
        k = n - len(g) - 1
        count = k * (k - 1) * (k - 2) // 6
        ans.append(count)

    print(*ans)


if __name__ == "__main__":
    main()
