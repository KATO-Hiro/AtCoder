# -*- coding: utf-8 -*-

from typing import Any, List, NamedTuple, Tuple

PENDING = -1


# See:
# https://docs.python.org/3/library/typing.html?highlight=namedtuple#typing.NamedTuple
class Edge(NamedTuple):
    frm: int = PENDING
    to: int = PENDING
    value: Any = PENDING


# See:
# https://drken1215.hatenablog.com/entry/2023/05/20/200517
class CycleDetection:
    pending: int = -1

    def __init__(self, vertex_count: int, graph: List[List[Tuple[int, int]]]) -> None:
        self.vertex_count: int = vertex_count
        self.graph: List[List[Tuple[int, int]]] = graph
        self.seen: List[bool] = [False] * self.vertex_count
        self.finished: List[bool] = [False] * self.vertex_count
        self.history: List[Any] = []

    def detect(self, is_prohibit_reverse: bool = True) -> List[Any]:
        pos = self.pending

        for vertex in range(self.vertex_count):
            if self.seen[vertex]:
                continue

            self.history.clear()
            pos = self._dfs(vertex, Edge(), is_prohibit_reverse)

            if pos != self.pending:
                return self.reconstruct(pos)

        return []

    def reconstruct(self, pos: int) -> List[int]:
        cycle: List[Any] = []

        while self.history:
            edge: Edge = self.history.pop()
            cycle.append(edge)

            if edge.frm == pos:
                break

        return cycle[::-1]

    def _dfs(self, cur: int, edge: Edge, is_prohibit_reverse: bool = True) -> int:
        self.seen[cur] = True
        self.history.append(edge)

        for to, id in self.graph[cur]:
            if is_prohibit_reverse and (to == edge.frm):
                continue
            if self.finished[to]:
                continue

            # Detected cycle.
            next_edge = Edge(cur, to, id)

            if self.seen[to] and not self.finished[to]:
                self.history.append(next_edge)
                return to

            pos = self._dfs(to, next_edge, is_prohibit_reverse)

            if pos != self.pending:
                return pos

        self.finished[cur] = True
        self.history.pop()
        return self.pending


def main():
    import sys

    sys.setrecursionlimit(10**8)

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    graph = [[] for _ in range(n)]

    for i, ai in enumerate(a):
        ai -= 1
        graph[i].append((ai, i))

    cd = CycleDetection(vertex_count=n, graph=graph)
    results = cd.detect(is_prohibit_reverse=False)

    print(len(results))

    ans = list()

    for frm, to, value in results:
        ans.append(value + 1)

    print(*ans)


if __name__ == "__main__":
    main()
