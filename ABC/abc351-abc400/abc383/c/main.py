# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import deque

    input = sys.stdin.readline

    h, w, d = map(int, input().split())
    # TODO: Change input format if needs.
    grid = [list(input().rstrip()) for _ in range(h)]

    q = deque()
    visited = [[False] * w for _ in range(h)]
    pending = -1
    dist = [[pending] * w for _ in range(h)]
    dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for i in range(h):
        for j in range(w):
            if grid[i][j] != "H":
                continue

            q.append((i, j))
            dist[i][j] = 0  # Initialize

    while q:
        y, x = q.popleft()

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
            if dist[y][x] >= d:
                continue

            dist[ny][nx] = dist[y][x] + 1  # Update ans
            q.append((ny, nx))

    ans = 0

    for i in range(h):
        for j in range(w):
            if dist[i][j] >= 0:
                ans += 1

    print(ans)


if __name__ == "__main__":
    main()
