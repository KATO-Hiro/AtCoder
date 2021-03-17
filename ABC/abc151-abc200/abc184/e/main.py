# -*- coding: utf-8 -*-


def main():
    from collections import deque
    import sys

    input = sys.stdin.readline

    h, w = map(int, input().split())
    a = [list(input().rstrip()) for _ in range(h)]
    sy, sx = 0, 0
    gy, gx = 0, 0
    inf = 10 ** 18
    dist = [[inf for _ in range(w)] for __ in range(h)]
    d = deque()
    dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    teleport = dict()

    for i in range(h):
        for j in range(w):
            if a[i][j] == "S":
                sy, sx = i, j
                dist[sy][sx] = 0
                d.append((sy, sx))
            elif a[i][j] == "G":
                gy, gx = i, j
            elif a[i][j].islower():
                if a[i][j] not in teleport.keys():
                    teleport[a[i][j]] = [(i, j)]
                else:
                    teleport[a[i][j]].append((i, j))

    while d:
        y, x = d.popleft()

        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy

            if nx < 0 or nx >= w:
                continue
            if ny < 0 or ny >= h:
                continue
            if a[ny][nx] == "#":
                continue
            if dist[ny][nx] != inf:
                continue

            dist[ny][nx] = dist[y][x] + 1
            d.append((ny, nx))

        if a[y][x].islower():
            if len(teleport[a[y][x]]) == 0:
                continue

            for ny, nx in teleport[a[y][x]]:
                if dist[ny][nx] != inf:
                    continue

                dist[ny][nx] = dist[y][x] + 1
                d.append((ny, nx))

            teleport[a[y][x]] = []

    if dist[gy][gx] == inf:
        print(-1)
    else:
        print(dist[gy][gx])


if __name__ == "__main__":
    main()
