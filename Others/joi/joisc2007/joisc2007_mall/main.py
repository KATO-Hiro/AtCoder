# -*- coding: utf-8 -*-


import sys

input = sys.stdin.readline

w, h = map(int, input().split())
wj, hi = map(int, input().split())
costs = [[0 for _ in range(w + 1)] for _ in range(h + 1)]
inf = 10**12
ans = inf

for i in range(h):
    ci = list(map(int, input().split()))

    for j, cij in enumerate(ci):
        if cij == -1:
            cij = inf

        costs[i + 1][j + 1] = costs[i + 1][j] + costs[i][j + 1] - costs[i][j] + cij

for i in range(h):
    for j in range(w):
        ni = i + hi - 1
        nj = j + wj - 1

        if ni >= h:
            break
        if nj >= w:
            break

        cost = costs[ni + 1][nj + 1] - costs[i][nj + 1] - costs[ni + 1][j] + costs[i][j]
        ans = min(ans, cost)

print(ans)
