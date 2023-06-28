# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import deque

    input = sys.stdin.readline

    r, c = map(int, input().split())
    sy, sx = map(int, input().split())
    sy -= 1
    sx -= 1
    gy, gx = map(int, input().split())
    gy -= 1
    gx -= 1
    grid = [list(input().rstrip()) for _ in range(r)]

    d = deque()
    d.append((sy, sx))
    inf = 10**9
    dist = [[inf for _ in range(c)] for _ in range(r)]
    dist[sy][sx] = 0
    dxy = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, -1), (-1, 1), (1, 1)]
    dxy = dxy[:4]
    visited = [[False for _ in range(c)] for _ in range(r)]

    while d:
        cur_y, cur_x = d.popleft()

        if visited[cur_y][cur_x]:
            continue

        visited[cur_y][cur_x] = True

        for dx, dy in dxy:
            nx = cur_x + dx
            ny = cur_y + dy

            if not (0 <= nx < c):
                continue
            if not (0 <= ny < r):
                continue
            if grid[ny][nx] == "#":
                continue

            dist[ny][nx] = min(dist[ny][nx], dist[cur_y][cur_x] + 1)
            d.append((ny, nx))

    print(dist[gy][gx])


if __name__ == "__main__":
    main()
