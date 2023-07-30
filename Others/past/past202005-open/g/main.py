# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import deque

    input = sys.stdin.readline

    n, y, x = map(int, input().split())
    size = 500
    c = [["." for _ in range(size)] for _ in range(size)]
    diff = 225
    y += diff
    x += diff

    for _ in range(n):
        yi, xi = map(int, input().split())
        yi += diff
        xi += diff
        c[yi][xi] = "#"

    d = deque()
    d.append((diff, diff))
    visited = [[False] * size for _ in range(size)]
    inf = 10**18
    dist = [[inf] * size for _ in range(size)]
    dist[diff][diff] = 0  # Initialize
    dxy = [(-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (1, -1)]

    while d:
        yj, xj = d.popleft()

        if visited[yj][xj]:
            continue

        visited[yj][xj] = True

        for dx, dy in dxy:
            nx = xj + dx
            ny = yj + dy

            if nx < 0 or nx >= size or ny < 0 or ny >= size:
                continue
            if visited[ny][nx]:
                continue
            if c[ny][nx] == "#":
                continue

            d.append((ny, nx))
            dist[ny][nx] = min(dist[ny][nx], dist[yj][xj] + 1)

    if visited[y][x]:
        print(dist[y][x])
    else:
        print(-1)


if __name__ == "__main__":
    main()
