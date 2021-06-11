# -*- coding: utf-8 -*-


def main():
    from collections import deque
    import sys

    input = sys.stdin.readline

    h, w = map(int, input().split())
    sy, sx = map(int, input().split())
    sy -= 1
    sx -= 1

    a = [list(map(int, input().split())) for _ in range(h)]
    visited = [[False for _ in range(w)] for _ in range(h)]
    d = deque()
    d.append((sy, sx))
    dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    ans = [["." for _ in range(w)] for _ in range(h)]
    ans[sy][sx] = "W"
    inf = 10 ** 9

    while d:
        cy, cx = d.popleft()
        visited[cy][cx] = True
        height = inf
        hy, hx = inf, inf

        for dx, dy in dxy:
            nx = cx + dx
            ny = cy + dy

            if nx < 0 or nx >= w:
                continue
            if ny < 0 or ny >= h:
                continue
            if visited[ny][nx]:
                continue

            if a[ny][nx] < a[cy][cx] and a[ny][nx] < height:
                height = a[ny][nx]
                hy, hx = ny, nx

        if height != inf:
            d.append((hy, hx))
            ans[hy][hx] = "W"

    for ai in ans:
        print("".join(map(str, ai)))


if __name__ == "__main__":
    main()
