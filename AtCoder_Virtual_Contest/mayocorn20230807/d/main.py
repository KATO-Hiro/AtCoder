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
        ans = 0

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
                ans = max(ans, dist[ny][nx])

        return ans

    ans = 0

    for i in range(h):
        for j in range(w):
            # 例外処理
            if s[i][j] == "#":
                continue

            result = bfs(i, j)
            ans = max(ans, result)

    print(ans)


if __name__ == "__main__":
    main()
