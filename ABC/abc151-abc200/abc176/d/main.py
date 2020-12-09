# -*- coding: utf-8 -*-


def main():
    from collections import deque

    h, w = map(int, input().split())
    sy, sx = map(int, input().split())
    gy, gx = map(int, input().split())
    sy -= 1
    sx -= 1
    gy -= 1
    gx -= 1
    s = [list(input()) for _ in range(h)]

    dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    INF = 10 ** 9
    dist = [[INF for _ in range(w)] for __ in range(h)]
    visited = [[False for _ in range(w)] for __ in range(h)]

    d = deque()
    d.append((sx, sy))
    dist[sy][sx] = 0
    visited[sy][sx] = True

    while d:
        xi, yi = d.popleft()

        for dx, dy in dxy:
            nx = xi + dx
            ny = yi + dy

            if nx < 0 or nx >= w:
                continue
            if ny < 0 or ny >= h:
                continue
            if s[ny][nx] == "#":
                continue
            if dist[ny][nx] <= dist[yi][xi]:
                continue

            visited[ny][nx] = True
            dist[ny][nx] = dist[yi][xi]
            d.appendleft((nx, ny))

        for i in range(-2, 2 + 1):
            for j in range(-2, 2 + 1):
                nx = xi + i
                ny = yi + j

                if nx < 0 or nx >= w:
                    continue
                if ny < 0 or ny >= h:
                    continue
                if s[ny][nx] == "#":
                    continue
                if dist[ny][nx] <= dist[yi][xi] + 1:
                    continue
                if visited[ny][nx]:
                    continue

                visited[ny][nx] = True
                dist[ny][nx] = dist[yi][xi] + 1
                d.append((nx, ny))

    ans = dist[gy][gx]

    if ans == INF:
        ans = -1

    print(ans)


if __name__ == "__main__":

    main()
