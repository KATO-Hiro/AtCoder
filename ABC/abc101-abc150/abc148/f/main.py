# -*- coding: utf-8 -*-


class TreeDistance:
    def __init__(self, vertex_count, graph) -> None:
        self.dist = [0 for _ in range(vertex_count)]
        self._graph = graph
        self._visited = [False for _ in range(vertex_count)]

    def calc(self, start_vertex):
        self._bfs(start_vertex)

        return self.dist

    def _bfs(self, vertex):
        from collections import deque

        d = deque()
        d.append(vertex)
        self._visited[vertex] = True

        while d:
            di = d.popleft()

            for to in self._graph[di]:
                if self._visited[to]:
                    continue

                self._visited[to] = True
                self.dist[to] = self.dist[di] + 1
                d.append(to)


def main():
    import sys

    input = sys.stdin.readline

    n, u, v = map(int, input().split())
    u -= 1
    v -= 1

    graph = [[] for _ in range(n)]

    for _ in range(n - 1):
        ai, bi = map(int, input().split())
        ai -= 1
        bi -= 1

        graph[ai].append(bi)
        graph[bi].append(ai)

    dist1 = TreeDistance(n, graph)
    takahashi_dist = dist1.calc(u)
    dist2 = TreeDistance(n, graph)
    aoki_dist = dist2.calc(v)

    dist_max = 0

    for t_dist, a_dist in zip(takahashi_dist, aoki_dist):
        if t_dist < a_dist:
            dist_max = max(dist_max, a_dist)

    ans = dist_max - 1
    print(ans)


if __name__ == "__main__":
    main()
