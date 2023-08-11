# -*- coding: utf-8 -*-

from typing import List


# See:
# https://ikatakos.com/pot/programming_algorithm/graph_theory/lowest_common_ancestor
# https://atcoder.jp/contests/codequeen2023-final-open/submissions/44445587
class Tree:
    def __init__(self, graph: List[List[int]], root=0) -> None:
        n = len(graph)
        k = n.bit_length()
        PENDING = -1

        # parent[k][u] := 2 ** k ahead of u.
        parent: List[List[int]] = [[PENDING] * n for _ in range(k)]
        depth: List[int] = [PENDING] * n
        depth[root] = 0
        stack: List[int] = [root]

        while stack:
            u = stack.pop()

            for v in graph[u]:
                if depth[v] != PENDING:
                    continue

                depth[v] = depth[u] + 1
                parent[0][v] = u
                stack.append(v)

        for ki in range(k - 1):
            for u in range(n):
                if parent[ki][u] < 0:
                    parent[ki + 1][u] = -1
                else:
                    parent[ki + 1][u] = parent[ki][parent[ki][u]]

        self.n: int = n
        self.k: int = k
        self.parent: List[List[int]] = parent
        self.depth: List[int] = depth

    def lca(self, u: int, v: int) -> int:
        depth, parent = self.depth, self.parent

        if depth[u] < depth[v]:
            u, v = v, u

        for ki in range(self.k):
            if (depth[u] - depth[v]) >> ki & 1:
                u = parent[ki][u]

        if u == v:
            return u

        for ki in range(self.k - 1, -1, -1):
            if parent[ki][u] != parent[ki][v]:
                u = parent[ki][u]
                v = parent[ki][v]

        return parent[0][u]

    def calc_dist(self, u: int, v: int) -> int:
        return self.depth[u] + self.depth[v] - 2 * self.depth[self.lca(u, v)]

    def is_on_path(self, u: int, v: int, a: int) -> bool:
        return self.calc_dist(u, a) + self.calc_dist(a, v) == self.calc_dist(u, v)


def main():
    import sys

    input = sys.stdin.readline

    n, s, t = map(int, input().split())
    s -= 1
    t -= 1

    graph = [[] for _ in range(n)]

    for _ in range(n - 1):
        ai, bi = map(int, input().split())
        ai -= 1
        bi -= 1

        graph[ai].append(bi)
        graph[bi].append(ai)

    # 頂点Sを根とする根付き木を考える
    # 最小共通祖先の頂点a = LCA(j, T)を求める
    # パスj→Tまでの最短経路のうち、頂点S→jまでの最短経路にも含まれる頂点集合は、頂点j→頂点aまで
    tree = Tree(graph=graph, root=s)
    ans = list()

    for j in range(n):
        lca = tree.lca(j, t)
        dist = tree.calc_dist(j, lca)
        ans.append(dist + 1)

    print(*ans, sep="\n")


if __name__ == "__main__":
    main()
