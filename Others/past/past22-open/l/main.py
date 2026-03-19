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

    def sort(self, force_unique=True) -> Tuple[bool, List[int]]:
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
            # No more than two vertices with indegree 0 are allowed.
            if force_unique and len(que) >= 2:
                return False, []

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

    input = sys.stdin.readline

    n = int(input())
    s = [list(input().rstrip()) for _ in range(n)]

    ts = TopologicalSorting(n)

    for i in range(n):
        for j in range(n):
            if s[i][j] != "o":
                continue

            ts.add_edge(frm=i, to=j)

    is_DAG, orders = ts.sort(force_unique=False)

    if is_DAG:
        print("Yes")

        pending = -1
        ranks = [pending] * n

        for id, order in enumerate(orders[::-1]):
            ranks[order] = id

        for i in range(n):
            for j in range(n):
                if s[i][j] != "?":
                    continue

                if ranks[i] > ranks[j]:
                    s[i][j] = "o"
                else:
                    s[i][j] = "x"

        for si in s:
            print("".join(si))
    else:
        print("No")


if __name__ == "__main__":
    main()
