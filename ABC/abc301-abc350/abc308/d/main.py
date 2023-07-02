# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import deque

    input = sys.stdin.readline

    h, w = map(int, input().split())
    # TODO: Change input format if needs.
    s = [list(input().rstrip()) for _ in range(h)]
    d = deque()
    d.append((0, 0, 0))
    visited = [[False] * w for _ in range(h)]
    dist = [[0] * w for _ in range(h)]
    dist[0][0] = 1  # Initialize
    dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    u = "snuke"

    while d:
        y, x, i = d.popleft()

        if visited[y][x]:
            continue

        if s[y][x] != u[i % 5]:
            continue

        visited[y][x] = True

        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy

            if nx < 0 or nx >= w or ny < 0 or ny >= h:
                continue
            if visited[ny][nx]:
                continue
            if s[ny][nx] != u[(i + 1) % 5]:
                continue

            d.append((ny, nx, i + 1))
            dist[ny][nx] = dist[y][x] + 1  # Update ans

    result = visited[h - 1][w - 1]

    if result:
        print("Yes")
    else:
        print("No")
    # print(result)
    # print(visited)


if __name__ == "__main__":
    main()
