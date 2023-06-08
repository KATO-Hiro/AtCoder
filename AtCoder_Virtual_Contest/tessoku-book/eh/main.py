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

    ans = -1
    count = 0

    for i in range(n):
        size = len(graph[i])

        if size > count:
            ans = i + 1
            count = size

    print(ans)


if __name__ == "__main__":
    main()
