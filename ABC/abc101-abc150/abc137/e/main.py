# -*- coding: utf-8 -*-


def bellman_ford(
    vertex_count: int,
    edges,
    reachables=None,
    dist_max: int = 10 ** 18,
    start: int = 0
):
    dist = [dist_max] * vertex_count
    dist[start] = 0

    if reachables is None:
        reachables = [True] * vertex_count

    is_updated = True
    step_count = 0
    has_cycle = False

    while is_updated:
        is_updated = False

        for ci, ai, bi in edges:
            if not reachables[ai] or not reachables[bi]:
                continue

            new_cost = dist[ai] + ci

            if new_cost < dist[bi]:
                dist[bi] = new_cost
                is_updated = True

        step_count += 1

        if step_count > vertex_count:
            has_cycle = True
            break

    return has_cycle, dist


def main():
    import sys

    sys.setrecursionlimit(10 ** 7)
    input = sys.stdin.readline

    n, m, p = map(int, input().split())
    graph1 = [[] for _ in range(n)]
    graph2 = [[] for _ in range(n)]
    edges = list()

    for i in range(m):
        ai, bi, ci = map(int, input().split())
        ai -= 1
        bi -= 1
        ci -= p  # コストを最初に除外
        ci *= -1  # 最長経路問題から最短経路問題に言い換えるため、符号を反転させる

        graph1[ai].append(bi)
        graph2[bi].append(ai)
        edges.append((ci, ai, bi))

    # 前処理: 頂点1から頂点N / 頂点Nから頂点1に到達できる頂点の集合を求める
    reachable_from_1 = [False] * n
    reachable_from_n = [False] * n

    def dfs1(v):
        if reachable_from_1[v]:
            return

        reachable_from_1[v] = True

        for to in graph1[v]:
            dfs1(to)

    def dfs2(v):
        if reachable_from_n[v]:
            return

        reachable_from_n[v] = True

        for to in graph2[v]:
            dfs2(to)

    dfs1(0)
    dfs2(n - 1)

    reachables = [False] * n

    for i, (case1, case2) in enumerate(zip(reachable_from_1, reachable_from_n)):
        if case1 and case2:
            reachables[i] = True

    # Bellman-Ford法
    has_cycle, dist = bellman_ford(n, edges, reachables)

    if has_cycle:
        print(-1)
    else:
        ans = max(0, -dist[n - 1])  # 最初に行った符号反転を元に戻す
        print(ans)


if __name__ == "__main__":
    main()
