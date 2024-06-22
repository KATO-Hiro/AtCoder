# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import deque
    from typing import Any, List, Tuple

    input = sys.stdin.readline

    h, w = map(int, input().split())
    grid = [list(input().rstrip()) for _ in range(h)]
    n = int(input())
    medicines = list()

    sy, sx, ty, tx = 0, 0, 0, 0

    for i in range(h):
        for j in range(w):
            if grid[i][j] == "S":
                sy, sx = i, j
            elif grid[i][j] == "T":
                ty, tx = i, j

    # スタートとゴールにもエネルギーが0の薬があるとみなす
    for _ in range(n):
        ri, ci, ei = list(map(int, input().split()))
        ri -= 1
        ci -= 1
        medicines.append((ri, ci, ei))

    medicines.append((sy, sx, 0))
    medicines.append((ty, tx, 0))
    inf = 10**12

    # 各薬を頂点とするグラフをBFSで求める
    def bfs_for_grid(
        grid: List[List[Any]], h: int, w: int, sy: int = 0, sx: int = 0
    ) -> List[List[int]]:
        d = deque()
        d.append((sy, sx))
        pending = inf
        dist = [[pending] * w for _ in range(h)]
        dist[sy][sx] = 0  # Initialize
        dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while d:
            y, x = d.popleft()

            if dist[y][x] == pending:
                continue

            for dx, dy in dxy:
                nx = x + dx
                ny = y + dy

                if nx < 0 or nx >= w or ny < 0 or ny >= h:
                    continue
                if grid[ny][nx] == "#":
                    continue
                if dist[ny][nx] != pending:
                    continue

                dist[ny][nx] = dist[y][x] + 1  # Update ans
                d.append((ny, nx))

        return dist

    to = [[] for _ in range(n + 2)]

    for i, (ri, ci, ei) in enumerate(medicines):
        dist = bfs_for_grid(grid=grid, h=h, w=w, sy=ri, sx=ci)

        # 薬jまで到達できるか判定
        for j, (rj, cj, _) in enumerate(medicines):
            if i == j:
                continue

            if dist[rj][cj] <= ei:
                to[i].append(j)

    # 到達判定
    def bfs_for_graph(
        vertex_count: int, graph: List[List[int]], start_id: int
    ) -> Tuple[List[bool], List[int]]:
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

    start_id = -2
    _, reachables = bfs_for_graph(vertex_count=n + 2, graph=to, start_id=start_id)

    if reachables[-1] == inf:
        print("No")
    else:
        print("Yes")


if __name__ == "__main__":
    main()
