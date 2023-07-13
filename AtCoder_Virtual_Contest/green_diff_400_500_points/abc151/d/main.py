# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import deque

    input = sys.stdin.readline

    h, w = map(int, input().split())
    # TODO: Change input format if needs.
    s = [list(input().rstrip()) for _ in range(h)]

    def bfs(i, j):
        d = deque()
        d.append((i, j))
        visited = [[False] * w for _ in range(h)]
        dist = [[0] * w for _ in range(h)]
        dist[i][j] = 0  # Initialize
        dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        dist_max = 0

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
                if s[ny][nx] == "#":
                    continue

                d.append((ny, nx))
                dist[ny][nx] = dist[y][x] + 1  # Update ans
                dist_max = max(dist_max, dist[ny][nx])

        return dist_max

    ans = 0

    # 始点を全探索
    for i in range(h):
        for j in range(w):
            if s[i][j] == "#":
                continue

            dist = bfs(i, j)
            ans = max(ans, dist)

    print(ans)


if __name__ == "__main__":
    main()
