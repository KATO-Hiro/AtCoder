# -*- coding: utf-8 -*-


def main():
    from collections import deque
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    dxy = list()

    # 前計算: 到達可能なマスを列挙
    for dx in range(-n, n):
        for dy in range(-n, n):
            if (dx ** 2 + dy ** 2) == m:
                dxy.append((dx, dy))
    
    # BFS
    not_visited = -1
    dist = [[not_visited] * n for _ in range(n)]
    dist[0][0] = 0
    d = deque()
    d.append((0, 0, 0))  # cur_dist, x, y

    while d:
        di, x, y = d.popleft()

        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if dist[ny][nx] == -1:
                dist[ny][nx] = di + 1
                d.append((di + 1, nx, ny))

    for di in dist:
        print(*di)


if __name__ == "__main__":
    main()
