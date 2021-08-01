# -*- coding: utf-8 -*-


from typing import Tuple


class TreeDiameter:
    def __init__(self, vertex_count: int, graph) -> None:
        self.vertex_count = vertex_count
        self.graph = graph

    def calc(self, source: int) -> Tuple[int, int, int]:
        p, _ = self._find_farthest_vertex(source=source)
        q, dist_max = self._find_farthest_vertex(source=p)

        return dist_max, p, q

    def _find_farthest_vertex(self, source: int) -> Tuple[int, int]:
        from collections import deque

        visited = [False for _ in range(self.vertex_count)]

        d = deque()
        d.append((0, source))

        farthest_vertex = 0
        dist_max = 0

        while d:
            dist, vertex = d.popleft()

            if visited[vertex]:
                continue

            visited[vertex] = True

            for weight, v in self.graph[vertex]:
                new_dist = dist + weight
                d.append((new_dist, v))

                if new_dist > dist_max:
                    farthest_vertex = v
                    dist_max = new_dist

        return farthest_vertex, dist_max


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())

    graph = [[] for _ in range(n)]

    for _ in range(n - 1):
        ai, bi = map(int, input().split())
        ai -= 1
        bi -= 1

        # ci: cost
        ci = 1
        graph[ai].append((ci, bi))
        graph[bi].append((ci, ai))

    tree_diameter = TreeDiameter(vertex_count=n, graph=graph)
    dist, _, _ = tree_diameter.calc(source=0)

    print(dist + 1)



if __name__ == "__main__":
    main()
