# -*- coding: utf-8 -*-


def calc_depth(vertex_count: int, graph):
    from collections import deque

    PENDING = -1
    depth = [PENDING for _ in range(vertex_count)]
    parent = [PENDING for _ in range(vertex_count)]
    depth[0], parent[0] = 0, 0
    d = deque()
    d.append(0)

    while d:
        vertex = d.popleft()

        for g in graph[vertex]:
            if depth[g] == PENDING:
                depth[g] = depth[vertex] + 1
                parent[g] = vertex
                d.append(g)

    return depth


def run_imos(graph, depth, imos):
    from collections import deque

    d = deque()
    d.append(0)

    while d:
        vertex = d.popleft()

        for g in graph[vertex]:
            if depth[vertex] < depth[g]:
                imos[g] += imos[vertex]
                d.append(g)

    return imos


def main():
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

    depth = calc_depth(vertex_count=n, graph=graph)

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

    print(*run_imos(graph=graph, depth=depth, imos=imos), sep="\n")


if __name__ == "__main__":
    main()
