# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import deque

    input = sys.stdin.readline

    n, m = map(int, input().split())

    # ユークリッド距離がsqrt(m)となるマスの移動量(x、y方向)dx, dyを求める
    dxy = set()

    for i in range(10**3 + 1):
        for j in range(10**3 + 1):
            if i**2 + j**2 == m:
                dxy.add((i, j))
                dxy.add((-i, j))
                dxy.add((i, -j))
                dxy.add((-i, -j))

    # BFS
    d = deque()
    d.append((0, 0))
    visited = [[False] * n for _ in range(n)]
    pending = -1
    cost = [[pending] * n for _ in range(n)]
    cost[0][0] = 0  # Initialize

    while d:
        y, x = d.popleft()

        if visited[y][x]:
            continue

        visited[y][x] = True

        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if visited[ny][nx]:
                continue
            if cost[ny][nx] != pending:
                continue

            d.append((ny, nx))
            cost[ny][nx] = cost[y][x] + 1  # Update ans

    for c in cost:
        print(*c)


if __name__ == "__main__":
    main()
