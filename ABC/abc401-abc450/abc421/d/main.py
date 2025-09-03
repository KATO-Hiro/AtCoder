# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import deque

    input = sys.stdin.readline

    h, w = map(int, input().split())
    a = [list(input().rstrip()) for _ in range(h)]
    inf = 10**18
    dist = [[[inf for _ in range(w + 10)] for _ in range(h + 10)] for _ in range(2)]
    q = deque()

    def push(i, j, state, di):
        if dist[state][i][j] != inf:
            return

        dist[state][i][j] = di
        q.append((i, j, state))

    sy, sx = -1, -1

    for i in range(h):
        for j in range(w):
            if a[i][j] == "S":
                sy, sx = i, j
                break

    push(sy, sx, 0, 0)
    dxy = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, -1), (-1, 1), (1, 1)]
    dxy = dxy[:4]

    while q:
        y, x, is_on = q.popleft()
        di = dist[is_on][y][x]

        if a[y][x] == "G":
            print(di)
            exit()

        for dx, dy in dxy:
            ny, nx = y + dy, x + dx
            nis_on = is_on

            if not (0 <= ny < h):
                continue
            if not (0 <= nx < w):
                continue
            if a[ny][nx] == "#":
                continue
            if not nis_on and a[ny][nx] == "x":
                continue
            if nis_on and a[ny][nx] == "o":
                continue

            if a[ny][nx] == "?":
                nis_on ^= 1

            push(ny, nx, nis_on, di + 1)

    print(-1)


if __name__ == "__main__":
    main()
