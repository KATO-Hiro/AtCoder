# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import deque

    input = sys.stdin.readline

    h, w = map(int, input().split())
    sy, sx = map(int, input().split())
    sy -= 1
    sx -= 1
    grid = [list(input().rstrip()) for _ in range(h)]

    d = deque()
    d.append((sy, sx))
    ans = [["x"] * w for _ in range(h)]
    ans[sy][sx] = "o"
    visited = [[False] * w for _ in range(h)]
    dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for i in range(h):
        for j in range(w):
            if grid[i][j] != "#":
                continue

            ans[i][j] = "#"

    while d:
        y, x = d.popleft()

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
            if grid[ny][nx] == "<" and dx != 1:
                continue
            if grid[ny][nx] == ">" and dx != -1:
                continue
            if grid[ny][nx] == "^" and dy != 1:
                continue
            if grid[ny][nx] == "v" and dy != -1:
                continue
            if ans[ny][nx] != "x":
                continue

            ans[ny][nx] = "o"
            d.append((ny, nx))

    for ans_i in ans:
        print("".join(ans_i))


if __name__ == "__main__":
    main()
