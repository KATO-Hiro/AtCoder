# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import deque

    input = sys.stdin.readline

    n = int(input())
    h, w = n, n
    sy, sx = map(lambda x: int(x) - 1, input().split())
    gy, gx = map(lambda x: int(x) - 1, input().split())
    # TODO: Change input format if needs.
    c = [list(input().rstrip()) for _ in range(h)]
    d = deque()
    d.append((sy, sx))
    visited = [[False] * w for _ in range(h)]
    pending = -1
    dist = [[pending] * w for _ in range(h)]
    dist[sy][sx] = 0  # Initialize
    dxy = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

    while d:
        y, x = d.popleft()

        if y == gy and x == gx:
            break

        if visited[y][x]:
            continue

        if dist[y][x] == pending:
            continue

        visited[y][x] = True

        for dx, dy in dxy:
            ny, nx = y + dy, x + dx

            while True:
                if nx < 0 or nx >= w or ny < 0 or ny >= h:
                    break
                if visited[ny][nx]:
                    break
                if c[ny][nx] == "#":
                    break
                if dist[ny][nx] != pending and (dist[ny][nx] <= dist[y][x]):
                    break

                # if dist[ny][nx] < dist[y][x]:
                d.append((ny, nx))
                dist[ny][nx] = dist[y][x] + 1  # Update ans

                nx += dx
                ny += dy

    ans = dist[gy][gx]

    print(ans)


if __name__ == "__main__":
    main()
