# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline
    from collections import deque

    n, m = map(int, input().split())

    # ある頂点vを決め打ちしたときに、残りの全ての頂点に移動できる = DFS / BFS
    # 最強が確定 = vが一つのみ
    graph = [[] for _ in range(n)]

    for _ in range(m):
        ai, bi = map(int, input().split())
        ai -= 1
        bi -= 1

        graph[ai].append(bi)

    inf = 10**18

    def bfs(vertex_count, graph, start_id):
        d = deque([start_id])
        visited = [False] * vertex_count
        dist = [inf] * vertex_count
        dist[start_id] = 0

        while d:
            cur = d.pop()

            if visited[cur]:
                continue

            visited[cur] = True

            for to in graph[cur]:
                if visited[to]:
                    continue

                d.append(to)
                dist[to] = min(dist[to], dist[cur] + 1)

        return visited, dist

    ans = list()

    for i in range(n):
        visited, dist = bfs(vertex_count=n, graph=graph, start_id=i)

        if dist.count(inf) == 0:
            ans.append(i + 1)
            # print(dist)

    if len(ans) == 1:
        print(*ans)
    else:
        print(-1)


if __name__ == "__main__":
    main()
