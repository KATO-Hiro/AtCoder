# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    graph = [set() for _ in range(n)]
    pairs = []

    for i in range(n):
        ai, bi = map(int, input().split())
        ai -= 1
        bi -= 1

        pairs.append((i, ai))
        graph[i].add(bi)

    used = [False] * n
    ans = 0

    for u, v in pairs:
        if used[u] or used[v]:
            continue

        for candidate in graph[u]:
            if candidate in graph[v]:
                ans += 1

        used[u] = True
        used[v] = True

    print(ans)


if __name__ == "__main__":
    main()
