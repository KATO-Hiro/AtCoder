# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    from collections import deque
    from typing import Any, List, Tuple

    h, w = map(int, input().split())
    # TODO: Change input format if needs.
    grid = [list(input().rstrip()) for _ in range(h)]
    sy, sx = 0, 0
    snuke = "snuke"

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

            if snuke[dist[y][x] % 5] != grid[y][x]:
                continue

            visited[y][x] = True

            for dx, dy in dxy:
                nx = x + dx
                ny = y + dy

                if nx < 0 or nx >= w or ny < 0 or ny >= h:
                    continue
                if visited[ny][nx]:
                    continue
                if dist[ny][nx] != pending and dist[ny][nx] <= dist[y][x]:
                    continue
                if snuke[(dist[y][x] + 1) % 5] != grid[ny][nx]:
                    continue

                dist[ny][nx] = dist[y][x] + 1  # Update ans
                d.append((ny, nx))

        return visited, dist

    visited, dist = bfs_for_grid(grid=grid, h=h, w=w, sy=sy, sx=sx)

    if dist[h - 1][w - 1] == -1:
        print("No")
    else:
        print("Yes")


if __name__ == "__main__":
    main()
