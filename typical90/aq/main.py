# -*- coding: utf-8 -*-


def main():
    from collections import deque
    import sys

    input = sys.stdin.readline

    h, w = map(int, input().split())
    rs, cs = map(lambda x: int(x) - 1, input().split())
    rt, ct = map(lambda x: int(x) - 1, input().split())
    s = [input().rstrip() for _ in range(h)]
    inf = 10 ** 6 + 10
    dist = [[inf] * w for _ in range(h)]
    dist[rs][cs] = 0
    dxy = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    d = deque() 

    for dir in range(4):
        d.append((rs, cs, dir, 0))

    while d:
        y, x, pre_dir, cost = d.popleft()

        if dist[y][x] < cost:
            continue

        for dir, (dx, dy) in enumerate(dxy):
            nx = x + dx
            ny = y + dy

            if nx < 0 or ny < 0 or nx >= w or ny >= h:
                continue
            if s[ny][nx] == "#":
                continue

            if pre_dir == dir:
                if dist[ny][nx] >= cost:
                    dist[ny][nx] = cost
                    d.appendleft((ny, nx, dir, cost))
            else:
                if dist[ny][nx] > cost:
                    dist[ny][nx] = cost + 1
                    d.append((ny, nx, dir, cost + 1))

    print(dist[rt][ct])


if __name__ == "__main__":
    main()
