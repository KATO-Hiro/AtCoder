# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import deque
    from typing import Any, List, Tuple

    input = sys.stdin.readline

    n, m = map(int, input().split())
    inf = 10**18
    graph = [[] for _ in range(n)]

    for _ in range(m):
        ai, bi = map(int, input().split())
        ai -= 1
        bi -= 1

        graph[ai].append(bi)

    def bfs_for_graph(
        vertex_count: int, graph: List[List[int]], start_id: int
    ) -> Tuple[List[bool], List[int]]:
        d = deque([start_id])
        visited = [False] * vertex_count
        dist = [inf] * vertex_count
        dist[start_id] = 0

        while d:
            cur = d.popleft()

            if visited[cur]:
                continue

            visited[cur] = True

            for to in graph[cur]:
                if visited[to]:
                    continue

                d.append(to)
                dist[to] = min(dist[to], dist[cur] + 1)

        return visited, dist

    start_id = 0
    visited, dist = bfs_for_graph(vertex_count=n, graph=graph, start_id=start_id)
    ans = sum([1 for v in visited if v])
    print(ans)


if __name__ == "__main__":
    main()
