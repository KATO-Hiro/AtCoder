# -*- coding: utf-8 -*-


def main():
    from collections import deque
    import sys

    input = sys.stdin.readline

    h, w = map(int, input().split())
    c = [list(input().rstrip()) for _ in range(h)]
    d = deque()
    d.append((0, 0))
    visited = [[False] * w for _ in range(h)]
    count = [[0] * w for _ in range(h)]
    count[0][0] = 1
    dxy = [(1, 0), (0, 1)]
    ans = 1

    while d:
        y, x = d.popleft()

        if visited[y][x]:
            continue

        visited[y][x] = True

        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy

            if nx < 0 or nx >= w or ny < 0 or ny >= h:
                continue
            if visited[ny][nx]:
                continue
            if c[ny][nx] == '#':
                continue

            d.append((ny, nx))
            count[ny][nx] = count[y][x] + 1
            ans = max(ans, count[ny][nx])

    print(ans)


if __name__ == "__main__":
    main()
