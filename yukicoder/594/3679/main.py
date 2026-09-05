# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import deque

    input = sys.stdin.readline

    h, w = map(int, input().split())
    a, b = map(int, input().split())
    r1, c1, r2, c2 = map(int, input().split())
    p, q = map(int, input().split())
    a -= 1
    b -= 1
    r1 -= 1
    c1 -= 1
    r2 -= 1
    c2 -= 1
    p -= 1
    q -= 1
    # TODO: Change input format if needs.
    grid = [[None] * w for _ in range(h)]

    def bfs_for_grid(
        grid: list[list[any]], h: int, w: int, sy: int = 0, sx: int = 0
    ) -> tuple[list[list[bool]], list[list[int]]]:
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

                dist[ny][nx] = dist[y][x] + 1  # Update ans
                d.append((ny, nx))

        return visited, dist

    _, dist1 = bfs_for_grid(grid=grid, h=h, w=w, sy=a, sx=b)
    _, dist2 = bfs_for_grid(grid=grid, h=h, w=w, sy=p, sx=q)
    inf = 10**18
    ans = inf

    for i in range(h):
        for j in range(w):
            candidate = 0

            if not (r1 <= i <= r2):
                continue
            if not (c1 <= j <= c2):
                continue

            candidate += dist1[i][j] + dist2[i][j] + dist2[a][b]
            ans = min(ans, candidate)

    print(ans)


if __name__ == "__main__":
    main()
