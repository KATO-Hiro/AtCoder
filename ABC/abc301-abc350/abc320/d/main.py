# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict, deque
    from typing import List, Tuple

    input = sys.stdin.readline

    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]

    for _ in range(m):
        ai, bi, xi, yi = map(int, input().split())
        ai -= 1
        bi -= 1

        # if ai > bi:
        #     ai, bi = bi, ai
        #     xi *= -1
        #     yi *= -1

        graph[ai].append((bi, xi, yi))
        graph[bi].append((ai, -xi, -yi))  # non-directed

    inf = 10**18

    def bfs_for_graph(vertex_count: int, graph: List[List[int]], start_id: int):
        d = deque()
        d.append((start_id, 0, 0))
        visited = [False] * vertex_count
        dist = defaultdict(tuple)
        dist[0] = (0, 0)

        while d:
            cur, xi, yi = d.pop()

            if visited[cur]:
                continue

            visited[cur] = True

            for to, xj, yj in graph[cur]:
                nx = xi + xj
                ny = yi + yj

                if visited[to]:
                    if to in dist.keys():
                        x, y = dist[to]

                        if x != nx or y != ny:
                            dist[to] = (inf, inf)

                        continue

                dist[to] = (nx, ny)
                d.append((to, nx, ny))

        return visited, dist

    start_id = 0
    visited, dist = bfs_for_graph(vertex_count=n, graph=graph, start_id=start_id)

    for i in range(n):
        if dist[i] == tuple():
            print("undecidable")
            continue

        xi, yi = dist[i]

        if (xi, yi) == (inf, inf):
            print("undecidable")
        else:
            print(xi, yi)


if __name__ == "__main__":
    main()
