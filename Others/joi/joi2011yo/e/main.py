# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict, deque
    from typing import Any, List, Tuple

    input = sys.stdin.readline

    h, w, n = map(int, input().split())
    s = [list(input().rstrip()) for _ in range(h)]
    pos = defaultdict(tuple)

    for i in range(h):
        for j in range(w):
            if s[i][j] == "." or s[i][j] == "X":
                continue

            if s[i][j] == "S":
                pos[0] = (i, j)
            else:
                pos[int(s[i][j])] = (i, j)

    # print(pos)

    def bfs_for_grid(
        grid: List[List[Any]], h: int, w: int, sy: int = 0, sx: int = 0, gy=-1, gx=-1
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

            if y == gy and x == gx:
                break

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
                if grid[ny][nx] == "X":
                    continue
                if dist[ny][nx] != pending and dist[ny][nx] <= dist[y][x]:
                    continue

                dist[ny][nx] = dist[y][x] + 1  # Update ans
                d.append((ny, nx))

        return visited, dist

    ans = 0

    for i in range(n):
        sy, sx = pos[i]
        # print(sy, sx)
        gy, gx = pos[i + 1]
        visited, dist = bfs_for_grid(grid=s, h=h, w=w, sy=sy, sx=sx, gy=gy, gx=gx)
        # print(dist)
        # print(gy, gx)
        ans += dist[gy][gx]

    print(ans)


if __name__ == "__main__":
    main()
