# -*- coding: utf-8 -*-


def main():
    import sys

    from collections import deque, defaultdict

    input = sys.stdin.readline

    h, w = map(int, input().split())
    # TODO: Change input format if needs.
    grid = [list(input().rstrip()) for _ in range(h)]

    d = defaultdict(list)

    for i in range(h):
        for j in range(w):
            cur = grid[i][j]

            if not cur.islower():
                continue

            d[cur].append((i, j))

    sy, sx = 0, 0
    pending = -1
    q = deque()
    q.append((sy, sx))
    dist = [[pending] * w for _ in range(h)]
    dist[sy][sx] = 0  # Initialize
    visited = [[False] * w for _ in range(h)]
    dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    used = set()

    while q:
        y, x = q.popleft()

        if dist[y][x] == pending:
            continue
        if visited[y][x]:
            continue

        visited[y][x] = True

        cur = grid[y][x]

        if cur.islower() and cur not in used:
            for ny, nx in d[cur]:
                if visited[ny][nx]:
                    continue
                if dist[ny][nx] != pending and dist[ny][nx] <= dist[y][x]:
                    continue

                dist[ny][nx] = dist[y][x] + 1
                q.append((ny, nx))

            used.add(cur)

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

            dist[ny][nx] = dist[y][x] + 1  # Update ans
            q.append((ny, nx))

    ans = dist[h - 1][w - 1]
    print(ans)


if __name__ == "__main__":
    main()
