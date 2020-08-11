# -*- coding: utf-8 -*-


def main():
    from collections import deque
    import sys
    input = sys.stdin.readline

    n, x, y = map(int, input().split())

    init = 500
    inf = 10 ** 4
    dist = [[init for _ in range(-201, 202)] for _ in range(-201, 202)]
    dist[0][0] = 0
    used = [[False for _ in range(-201, 202)] for _ in range(-201, 202)]
    used[0][0] = True
    d = deque()
    d.append((0, 0))
    dxy = [(-1, 1), (0, 1), (1, 1), (-1, 0), (1, 0), (0, -1)]

    for i in range(n):
        xi, yi = map(int, input().split())

        dist[xi][yi] = inf

    while d:
        dist_x, dist_y = d.popleft()

        for dx, dy in dxy:
            nx = dist_x + dx
            ny = dist_y + dy

            if (nx < 0) or (nx > 400) or (ny < 0) or (ny > 400):
                continue

            if dist[nx][ny] == inf:
                continue

            if used[nx][ny]:
                continue

            used[nx][ny] = True
            dist[nx][ny] = min(dist[nx][ny], dist[dist_x][dist_y] + 1)

            d.append((nx, ny))

    if dist[x][y] == init:
        print(-1)
    else:
        print(dist[x][y])


if __name__ == '__main__':
    main()
