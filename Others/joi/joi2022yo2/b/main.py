# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import deque

    input = sys.stdin.readline

    h, w = map(int, input().split())
    # TODO: Change input format if needs.
    s = [list(input().rstrip()) for _ in range(h)]
    d = deque()
    d.append((0, 0, s[0][0]))  # y, x, color
    visited = [[False] * w for _ in range(h)]
    pending = -1
    dist = [[pending] * w for _ in range(h)]
    dist[0][0] = 0  # Initialize
    dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while d:
        y, x, color = d.popleft()

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

            next_color = s[ny][nx]

            if next_color == color:
                continue

            if dist[ny][nx] != pending and dist[ny][nx] <= dist[y][x]:
                continue

            d.append((ny, nx, next_color))
            dist[ny][nx] = dist[y][x] + 1  # Update ans

    ans = dist[h - 1][w - 1]
    print(ans)


if __name__ == "__main__":
    main()
