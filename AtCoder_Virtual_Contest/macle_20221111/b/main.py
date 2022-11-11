# -*- coding: utf-8 -*-


def main():
    from collections import deque
    import sys

    input = sys.stdin.readline

    h, w = map(int, input().split())
    c = [list(input().rstrip()) for _ in range(h)]
    inf = -10 ** 18
    dist = [[inf] * w for _ in range(h)]
    dist[0][0] = 1
    d = deque()
    d.append((0, 0))
    dxy = [(0, 1), (1, 0)]
    visited = [[False] * w for _ in range(h)]
    ans = 1

    while d:
        y, x = d.popleft()

        if visited[y][x]:
            continue

        visited[y][x] = True

        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy

            if nx >= w or ny >= h:
                continue
            if c[ny][nx] == "#":
                continue

            dist[ny][nx] = dist[y][x] + 1
            d.append((ny, nx))
            ans = max(ans, dist[ny][nx])

    print(ans)


if __name__ == "__main__":
    main()
