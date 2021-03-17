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
    teleport = [[] for _ in range(26)]
    is_used = [False for _ in range(26)]

    for i in range(h):
        for j in range(w):
            if a[i][j] == "S":
                sy, sx = i, j
                dist[sy][sx] = 0
                d.append((sy, sx))
            elif a[i][j] == "G":
                gy, gx = i, j
            elif a[i][j].islower():
                diff = ord(a[i][j]) - ord("a")
                teleport[diff].append((i, j))

    while d:
        y, x = d.popleft()

        if y == gy and x == gx:
            print(dist[y][x])
            exit()

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
            diff = ord(a[y][x]) - ord("a")

            if is_used[diff]:
                continue

            for ny, nx in teleport[diff]:
                if dist[ny][nx] != inf:
                    continue

                dist[ny][nx] = dist[y][x] + 1
                d.append((ny, nx))

            is_used[diff] = True

    print(-1)


if __name__ == "__main__":
    main()
