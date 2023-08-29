# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import deque
    from typing import Any, List, Tuple

    input = sys.stdin.readline

    h, w = map(int, input().split())
    a = [list(input().rstrip()) for _ in range(h)]

    # 人の視線に入る部分をチェック
    # 共通部分をまとめる
    dxy = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, -1), (-1, 1), (1, 1)]
    dxy = dxy[:4]
    dirs = ["<", ">", "^", "v"]
    eye = "!"

    for (dx, dy), dir in zip(dxy, dirs):
        for i in range(h):
            for j in range(w):
                if a[i][j] != dir:
                    continue

                ny, nx = i, j

                while True:
                    ny += dy
                    nx += dx

                    if nx < 0 or nx >= w or ny < 0 or ny >= h:
                        break
                    if not (a[ny][nx] == "." or a[ny][nx] == eye):
                        break

                    a[ny][nx] = eye

    # 始点・終点の位置を調べる
    sy, sx, gy, gx = -1, -1, -1, -1

    for i in range(h):
        for j in range(w):
            if a[i][j] == "S":
                sy, sx = i, j
            elif a[i][j] == "G":
                gy, gx = i, j

    # BFSで始点から終点まで移動
    blocked = [">", "v", "<", "^", "#", "!"]

    def bfs_for_grid(
        grid: List[List[Any]], h: int, w: int, sy: int = 0, sx: int = 0
    ) -> Tuple[List[List[bool]], List[List[int]]]:
        d = deque()
        d.append((sy, sx))
        visited = [[False] * w for _ in range(h)]
        pending = -1
        dist = [[pending] * w for _ in range(h)]
        dist[sy][sx] = 0  # Initialize
        dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while d:
            y, x = d.popleft()

            if dist[y][x] == pending:
                continue

            if visited[y][x]:
                continue

            visited[y][x] = True

            for dx, dy in dxy:
                nx = x + dx
                ny = y + dy

                if nx < 0 or nx >= w or ny < 0 or ny >= h:
                    continue
                if visited[ny][nx]:
                    continue
                if grid[ny][nx] in blocked:
                    continue
                if dist[ny][nx] != pending and dist[ny][nx] <= dist[y][x]:
                    continue

                dist[ny][nx] = dist[y][x] + 1  # Update ans
                d.append((ny, nx))

        return visited, dist

    visited, dist = bfs_for_grid(grid=a, h=h, w=w, sy=sy, sx=sx)

    print(dist[gy][gx])


if __name__ == "__main__":
    main()
