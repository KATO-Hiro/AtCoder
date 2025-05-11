# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import deque

    input = sys.stdin.readline

    h, w = map(int, input().split())
    # TODO: Change input format if needs.
    grid = [list(input().rstrip()) for _ in range(h)]
    d = deque()
    pending = -1
    dist = [[pending] * w for _ in range(h)]

    for i in range(h):
        for j in range(w):
            if grid[i][j] == "E":
                d.append((i, j))
                dist[i][j] = 0  # Initialize

    visited = [[False] * w for _ in range(h)]
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
            if grid[ny][nx] == "#":
                continue
            if dist[ny][nx] != pending and dist[ny][nx] <= dist[y][x]:
                continue

            if dy == 1:
                grid[ny][nx] = "^"
            elif dy == -1:
                grid[ny][nx] = "v"
            elif dx == 1:
                grid[ny][nx] = "<"
            elif dx == -1:
                grid[ny][nx] = ">"

            dist[ny][nx] = dist[y][x] + 1  # Update ans
            d.append((ny, nx))

    for i in range(h):
        ans = "".join(grid[i])
        print(ans)


if __name__ == "__main__":
    main()
