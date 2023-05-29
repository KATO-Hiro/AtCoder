# -*- coding: utf-8 -*-


from collections import deque
from typing import List, Tuple


class TopologicalSorting:
    """
    See:
    https://atcoder.jp/contests/abc291/submissions/39241055
    """

    def __init__(self, vertex_count: int) -> None:
        self.vertex_count = vertex_count
        self.graph = [[] for _ in range(vertex_count)]
        self.indegrees = [0] * vertex_count

    def add_edge(self, frm: int, to: int) -> None:
        """
        Args:
            frm(from) -> to: Vertex number (0-indexed).
        """
        assert 0 <= frm < self.vertex_count
        assert 0 <= to < self.vertex_count

        self.graph[frm].append(to)
        self.indegrees[to] += 1

    def sort(self) -> Tuple[bool, List[int]]:
        """
        Returns:
            is_DAG: Is it DAG (Directed Acyclic Graph) ?
            orders: Order of vertices (0-indexed).
        """
        que = deque([i for i in range(self.vertex_count) if self.indegrees[i] == 0])
        results = list()

        if len(que) == 0:
            return False, []

        while que:
            # 起点となる頂点が複数存在してもok
            # if len(que) >= 2:
            #     return False, []

            vertex = que.popleft()
            results.append(vertex)

            for to in self.graph[vertex]:
                self.indegrees[to] -= 1

                if self.indegrees[to] == 0:
                    que.append(to)

        if len(results) == self.vertex_count:
            return True, results
        else:
            return False, []


def main():
    import sys
    from collections import defaultdict

    input = sys.stdin.readline

    n = int(input())
    a = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(n)]

    # 試合を頂点、各選手が行う試合の順番を有向グラフと捉える
    # DAG + 最長経路問題
    # 選手と試合のidの対応づけ
    ids = defaultdict(int)
    id = 0

    for i in range(n):
        for j in range(i + 1, n):
            ids[(i, j)] = id
            id += 1

    def to_id(i, j):
        if i > j:
            i, j = j, i

        return ids[(i, j)]

    vertex_count = n * (n - 1) // 2
    ts = TopologicalSorting(vertex_count)

    for i in range(n):
        # 選手番号から試合のidに変換
        for j in range(n - 1):
            a[i][j] = to_id(i, a[i][j])

        # 各選手に対して、指定された日程の順番に辺を張る
        for ui, vi in zip(a[i], a[i][1:]):
            ts.add_edge(vi, ui)
            # ts.add_edge(ui, vi)

    is_DAG, orders = ts.sort()

    if is_DAG:
        # 最長経路問題 = dp
        dp = [1] * vertex_count

        for i in range(vertex_count):
            for to in ts.graph[orders[i]]:
                dp[to] = max(dp[to], dp[orders[i]] + 1)

        print(max(dp))
    else:
        print(-1)


if __name__ == "__main__":
    main()
