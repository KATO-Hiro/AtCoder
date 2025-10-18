# -*- coding: utf-8 -*-


from collections import deque


def calc_depth(vertex_count: int, graph, source: int):
    PENDING = -1
    depth = [PENDING for _ in range(vertex_count)]
    depth[source] = 0
    d = deque([source])

    while d:
        vertex = d.popleft()

        for g in graph[vertex]:
            if depth[g] == PENDING:
                depth[g] = depth[vertex] + 1
                d.append(g)

    return depth


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    graph = [[] for _ in range(n)]

    for _ in range(n - 1):
        ai, bi = map(int, input().split())
        ai -= 1
        bi -= 1

        graph[ai].append(bi)
        graph[bi].append(ai)

    # 木の直径の両端(s, t)を求める
    # 同じ距離の場合は、(距離、頂点番号)の辞書順で比較
    dist_0 = calc_depth(n, graph, 0)
    s = max([(dist_0[i], i) for i in range(n)])[1]
    dist_s = calc_depth(n, graph, s)
    t = max([(dist_s[i], i) for i in range(n)])[1]
    dist_t = calc_depth(n, graph, t)

    for i in range(n):
        ans = max((dist_s[i], s), (dist_t[i], t))[1] + 1
        print(ans)


if __name__ == "__main__":
    main()
