# -*- coding: utf-8 -*-


from collections import deque
from typing import List, Tuple


class TopologicalSorting:
    def __init__(self, vertex_count: int) -> None:
        self.vertex_count = vertex_count
        self.graph = [[] for _ in range(vertex_count)]
        self.indegrees = [0] * vertex_count

    def add_edge(self, frm: int, to: int) -> None:
        assert 0 <= frm < self.vertex_count
        assert 0 <= to < self.vertex_count

        self.graph[frm].append(to)
        self.indegrees[to] += 1

    def sort(self) -> Tuple[bool, List[int]]:
        que = deque([i for i in range(self.vertex_count) if self.indegrees[i] == 0])
        results = list()

        if len(que) == 0:
            return False, []

        while que:
            if len(que) >= 2:
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

    n, m = map(int, input().split())
    ts = TopologicalSorting(n)

    for _ in range(m):
        ai, bi = map(int, input().split())
        ai -= 1
        bi -= 1

        ts.add_edge(frm=ai, to=bi)

    is_DAG, orders = ts.sort()

    if is_DAG:
        ans = [0] * n

        for i in range(n):
            ans[orders[i]] = i + 1

        print("Yes")
        print(*ans)
    else:
        print("No")


if __name__ == "__main__":
    main()
