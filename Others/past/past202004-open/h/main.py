# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import deque

    input = sys.stdin.readline

    h, w = map(int, input().split())
    a = [list(input().rstrip()) for _ in range(h)]

    # See:
    # https://blog.hamayanhamayan.com/entry/2020/05/06/225426
    # 最短経路問題 = BFS + 経路が指定されている = 直前の状態のみに関心 = 状態を一つ増やす
    d = deque()
    size = 15
    visited = [[[False] * size for _ in range(w)] for _ in range(h)]
    inf = 10**18
    dist = [[[inf] * size for _ in range(w)] for _ in range(h)]
    dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    sy, sx = -1, -1
    gy, gx = -1, -1

    for i in range(h):
        for j in range(w):
            if a[i][j] == "S":
                sy, sx = i, j
            if a[i][j] == "G":
                gy, gx = i, j

    d.append((sy, sx, 0))
    dist[sy][sx][0] = 0  # Initialize

    while d:
        y, x, state = d.popleft()

        if visited[y][x][state]:
            continue

        visited[y][x][state] = True

        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy

            if nx < 0 or nx >= w or ny < 0 or ny >= h:
                continue
            if visited[ny][nx][state]:
                continue
            if dist[ny][nx][state] != inf:
                continue

            d.append((ny, nx, state))
            dist[ny][nx][state] = dist[y][x][state] + 1

            if str(state + 1) != a[ny][nx]:
                continue
            if dist[ny][nx][state + 1] != inf:
                continue

            d.append((ny, nx, state + 1))
            dist[ny][nx][state + 1] = dist[y][x][state] + 1

    ans = dist[gy][gx][9]

    if ans == inf:
        ans = -1

    print(ans)


if __name__ == "__main__":
    main()
