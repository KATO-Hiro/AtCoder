# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import deque
    from typing import List, Tuple

    input = sys.stdin.readline

    n, m, q, k = map(int, input().split())
    a = list(map(lambda x: int(x) - 1, input().split()))
    graph = [[] for _ in range(n)]

    for _ in range(m):
        ui, vi = map(int, input().split())
        ui -= 1
        vi -= 1

        graph[ui].append(vi)
        graph[vi].append(ui)

    inf = 10**18

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

    dists = list()

    for start_id in a:
        _, dist = bfs_for_graph(vertex_count=n, graph=graph, start_id=start_id)
        dists.append(dist)

    for _ in range(q):
        si, ti = map(int, input().split())
        si -= 1
        ti -= 1
        ans = inf

        for dist in dists:
            dsi, dti = dist[si], dist[ti]

            if dsi == inf or dti == inf:
                continue

            candidate = dsi + dti
            ans = min(ans, candidate)

        print(ans)


if __name__ == "__main__":
    main()
