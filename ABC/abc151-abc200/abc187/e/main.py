# -*- coding: utf-8 -*-


def main():
    from collections import deque
    import sys

    input = sys.stdin.readline

    n = int(input())
    graph = [[] for _ in range(n)]
    a = [0 for _ in range(n - 1)]
    b = [0 for _ in range(n - 1)]

    for i in range(n - 1):
        ai, bi = map(int, input().split())
        ai -= 1
        bi -= 1
        a[i] = ai
        b[i] = bi

        graph[ai].append(bi)
        graph[bi].append(ai)

    depth = [-1 for _ in range(n)]
    depth[0] = 0
    d = deque()
    d.append(0)

    while d:
        vertex = d.popleft()

        for g in graph[vertex]:
            if depth[g] == -1:
                depth[g] = depth[vertex] + 1
                d.append(g)

    q = int(input())
    imos = [0 for _ in range(n)]

    for i in range(q):
        ti, ei, xi = map(int, input().split())
        ei -= 1

        va = a[ei]
        vb = b[ei]

        if ti == 2:
            va, vb = vb, va

        if depth[va] < depth[vb]:
            imos[0] += xi
            imos[vb] -= xi
        else:
            imos[va] += xi

    f = deque()
    f.append(0)

    while f:
        vertex = f.popleft()

        for g in graph[vertex]:
            if depth[vertex] < depth[g]:
                imos[g] += imos[vertex]
                f.append(g)

    print(*imos)


if __name__ == "__main__":
    main()
