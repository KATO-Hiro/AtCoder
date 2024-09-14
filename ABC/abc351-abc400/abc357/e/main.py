# -*- coding: utf-8 -*-

import sys
import typing


# See:
# https://github.com/not522/ac-library-python/tree/master/atcoder
class SCCGraph:
    def __init__(self, n: int = 0) -> None:
        self._internal = _SCCGraph(n)

    def add_edge(self, from_vertex: int, to_vertex: int) -> None:
        n = self._internal.num_vertices()

        assert 0 <= from_vertex < n
        assert 0 <= to_vertex < n

        self._internal.add_edge(from_vertex, to_vertex)

    def scc(self) -> typing.List[typing.List[int]]:
        return self._internal.scc()


class CSR:
    def __init__(self, n: int, edges: typing.List[typing.Tuple[int, int]]) -> None:
        self.start = [0] * (n + 1)
        self.elist = [0] * len(edges)

        for e in edges:
            self.start[e[0] + 1] += 1

        for i in range(1, n + 1):
            self.start[i] += self.start[i - 1]

        counter = self.start.copy()

        for e in edges:
            self.elist[counter[e[0]]] = e[1]
            counter[e[0]] += 1


class _SCCGraph:
    """
    Reference:
    R. Tarjan,
    Depth-First Search and Linear Graph Algorithms
    """

    def __init__(self, n: int) -> None:
        self._n = n
        self._edges: typing.List[typing.Tuple[int, int]] = []

    def num_vertices(self) -> int:
        return self._n

    def add_edge(self, from_vertex: int, to_vertex: int) -> None:
        self._edges.append((from_vertex, to_vertex))

    def scc_ids(self) -> typing.Tuple[int, typing.List[int]]:
        g = CSR(self._n, self._edges)
        now_ord = 0
        group_num = 0
        visited = []
        low = [0] * self._n
        order = [-1] * self._n
        ids = [0] * self._n

        sys.setrecursionlimit(max(self._n + 1000, sys.getrecursionlimit()))

        def dfs(v: int) -> None:
            nonlocal now_ord
            nonlocal group_num
            nonlocal visited
            nonlocal low
            nonlocal order
            nonlocal ids

            low[v] = now_ord
            order[v] = now_ord
            now_ord += 1
            visited.append(v)

            for i in range(g.start[v], g.start[v + 1]):
                to = g.elist[i]

                if order[to] == -1:
                    dfs(to)
                    low[v] = min(low[v], low[to])
                else:
                    low[v] = min(low[v], order[to])

            if low[v] == order[v]:
                while True:
                    u = visited[-1]
                    visited.pop()
                    order[u] = self._n
                    ids[u] = group_num

                    if u == v:
                        break

                group_num += 1

        for i in range(self._n):
            if order[i] == -1:
                dfs(i)

        for i in range(self._n):
            ids[i] = group_num - 1 - ids[i]

        return group_num, ids

    def scc(self) -> typing.List[typing.List[int]]:
        ids = self.scc_ids()
        group_num = ids[0]
        counts = [0] * group_num

        for x in ids[1]:
            counts[x] += 1

        groups: typing.List[typing.List[int]] = [[] for _ in range(group_num)]

        for i in range(self._n):
            groups[ids[1][i]].append(i)

        return groups


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(lambda x: int(x) - 1, input().split()))
    g = SCCGraph(n)

    # functional graph
    # 強連結成分分解を利用して、サイクルを見つける
    for i, ai in enumerate(a):
        g.add_edge(i, ai)

    counts = [0] * n

    # サイクルは末尾にあるので、逆順に処理
    for group in g.scc()[::-1]:
        size = len(group)
        g0 = group[0]

        # サイクル or 自己ループ
        if size >= 2 or g0 == a[g0]:
            for g in group:
                counts[g] = size
        else:
            # サイクルに近い頂点から + 1
            counts[g0] = counts[a[g0]] + 1

    print(sum(counts))


if __name__ == "__main__":
    main()
