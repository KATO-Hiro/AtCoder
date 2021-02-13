# -*- coding: utf-8 -*-


def main():
    from sys import setrecursionlimit
    import sys

    setrecursionlimit(10 ** 7)
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

    depth_list = [-1 for _ in range(n)]

    def calc_depth(vertex, depth):
        depth_list[vertex] = depth

        for g in graph[vertex]:
            if depth_list[g] == -1:
                calc_depth(g, depth + 1)

    calc_depth(0, 0)

    q = int(input())
    imos = [0 for _ in range(n)]

    for i in range(q):
        ti, ei, xi = map(int, input().split())
        ei -= 1

        va = a[ei]
        vb = b[ei]

        if ti == 2:
            va, vb = vb, va

        if depth_list[va] < depth_list[vb]:
            imos[0] += xi
            imos[vb] -= xi
        else:
            imos[va] += xi

    def apply_imos_method(vertex, current_value):
        imos[vertex] += current_value
        current_value = imos[vertex]

        for g in graph[vertex]:
            if depth_list[vertex] < depth_list[g]:
                apply_imos_method(g, current_value)

    apply_imos_method(0, 0)

    print(*imos)


if __name__ == "__main__":
    main()
