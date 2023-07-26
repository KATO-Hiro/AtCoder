# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import deque

    input = sys.stdin.readline

    a, b = map(int, input().split())
    a -= 1
    b -= 1
    s = [list(input().rstrip()) for _ in range(3)]
    dxy = [
        [(-1, -1), (-1, 0), (-1, 1)],
        [(0, -1), (0, 0), (0, 1)],
        [(1, -1), (1, 0), (1, 1)],
    ]

    ndxy = list()

    for i in range(3):
        for j in range(3):
            if s[i][j] == "#":
                ndxy.append(dxy[i][j])

    size = 9
    d = deque()
    d.append((a, b))
    visited = [[False] * size for _ in range(size)]

    while d:
        y, x = d.popleft()

        if visited[y][x]:
            continue

        visited[y][x] = True

        for dy, dx in ndxy:
            nx = x + dx
            ny = y + dy

            if nx < 0 or nx >= size or ny < 0 or ny >= size:
                continue
            if visited[ny][nx]:
                continue

            d.append((ny, nx))

    ans = 0

    for i in range(size):
        for j in range(size):
            if visited[i][j]:
                ans += 1

    print(ans)
    # print(visited)


if __name__ == "__main__":
    main()
