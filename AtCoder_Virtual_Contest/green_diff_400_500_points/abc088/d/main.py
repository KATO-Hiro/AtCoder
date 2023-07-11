# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import deque

    input = sys.stdin.readline

    h, w = map(int, input().split())
    s = [list(input().rstrip()) for _ in range(h)]

    # BFS
    # ゴールに到達できない = スタートからの最短距離がinf
    d = deque()
    d.append((0, 0))
    visited = [[False] * w for _ in range(h)]
    dist = [[0] * w for _ in range(h)]
    dist[0][0] = 1  # Initialize
    dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]

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

    if visited[h - 1][w - 1]:
        # スコア = 全体 - 最初から黒マスの数 - 最短経路を通るマス数
        ans = h * w - dist[h - 1][w - 1]

        for i in range(h):
            for j in range(w):
                if s[i][j] == "#":
                    ans -= 1

        print(ans)
    else:
        print(-1)


if __name__ == "__main__":
    main()
