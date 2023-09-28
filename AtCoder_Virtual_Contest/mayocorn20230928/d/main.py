# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import deque
    from typing import List, Tuple

    input = sys.stdin.readline

    n, x, y = map(int, input().split())
    x -= 1
    y -= 1
    graph = [[] for _ in range(n)]

    for i in range(n - 1):
        graph[i].append(i + 1)
        graph[i + 1].append(i)  # non-directed

    graph[x].append(y)
    graph[y].append(x)

    inf = 10**18

    def bfs_for_graph(
        vertex_count: int, graph: List[List[int]], start_id: int
    ) -> Tuple[List[bool], List[int]]:
        d = deque([start_id])
        visited = [False] * vertex_count
        dist = [inf] * vertex_count
        dist[start_id] = 0

        while d:
            cur = d.pop()

            for to in graph[cur]:
                if dist[cur] + 1 >= dist[to]:
                    continue

                d.append(to)
                dist[to] = min(dist[to], dist[cur] + 1)

        return visited, dist

    ans = [0] * n

    for start_id in range(n):
        visited, dist = bfs_for_graph(vertex_count=n, graph=graph, start_id=start_id)
        # print(dist)

        for j, di in enumerate(dist):
            if j > start_id:
                ans[di] += 1

    print(*ans[1:], sep="\n")


if __name__ == "__main__":
    main()
