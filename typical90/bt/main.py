# -*- coding: utf-8 -*-


import sys
sys.setrecursionlimit(10 ** 8)

h, w = map(int, input().split())
c = [list(input()) for _ in range(h)]
dist = [[-1] * w for _ in range(h)]
dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def dfs(x, y, length=0):
    global ans
    dist[y][x] = length

    if (x, y) == (i, j):
        ans = max(ans, length)

    for dx, dy in dxy:
        nx, ny = x + dx, y + dy

        if nx < 0 or ny < 0 or nx >= w or ny >= h:
            continue
        if c[ny][nx] == '#':
            continue
        if dist[ny][nx] > 0:
            continue

        dfs(nx, ny, length + 1)

    dist[y][x] = -1

ans = 0

for j in range(h):
    for i in range(w):
        if c[j][i] == '#':
            continue

        dfs(i, j)

if ans <= 2:
    print(-1)
else: 
    print(ans)
