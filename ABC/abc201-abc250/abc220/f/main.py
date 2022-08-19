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


def main():
    import sys

    input = sys.stdin.readline
    sys.setrecursionlimit(10 ** 7)

    n = int(input())
    graph = [[] for _ in range(n)]
    
    for _ in range(n - 1):
        ai, bi = map(int, input().split())
        ai -= 1
        bi -= 1
    
        graph[ai].append(bi)
        graph[bi].append(ai)

    # dist(1, j)を求める
    depth = calc_depth(n, graph)
    tree_size = [0] * n
    ans = [0] * n
    ans[0] = sum(depth)

    # 部分木のサイズを求める
    def dfs(vertex, parent=-1):
        tree_size[vertex] = 1

        for to in graph[vertex]:
            if to == parent:
                continue

            tree_size[vertex] += dfs(to, vertex)
        
        return tree_size[vertex]

    dfs(0)

    # 頂点1とそれ以外の頂点との差分の更新
    def dfs2(vertex, parent=-1):
        for to in graph[vertex]:
            if to == parent:
                continue

            ans[to] = ans[vertex] - tree_size[to] + (n - tree_size[to])
            dfs2(to, vertex)
    
    dfs2(0)
    print(*ans, sep='\n')


if __name__ == "__main__":
    main()
