# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import deque

    input = sys.stdin.readline

    h, w = map(int, input().split())
    s = [list(input().rstrip()) for _ in range(h)]
    dxy = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, -1), (-1, 1), (1, 1)]

    for _ in range(2):
        t = [["." for _ in range(w)] for _ in range(h)]

        for i in range(h):
            for j in range(w):
                if s[i][j] != "#":
                    continue

                for dx, dy in dxy:
                    ny, nx = i + dy, j + dx

                    if not (0 <= nx < w):
                        continue
                    if not (0 <= ny < h):
                        continue
                    if s[ny][nx] == "#":
                        continue

                    t[ny][nx] = "#"

        s = t[:]

    q = deque()
    inf = 10**18 + 1
    dist = [[inf for _ in range(w)] for _ in range(h)]

    for i in range(h):
        for j in range(w):
            if s[i][j] == ".":
                continue

            q.append((i, j))
            dist[i][j] = 0

    visited = [[False for _ in range(w)] for _ in range(h)]

    while q:
        y, x = q.popleft()

        if visited[y][x]:
            continue

        visited[y][x] = True

        for dx, dy in dxy:
            ny, nx = y + dy, x + dx

            if not (0 <= nx < w):
                continue
            if not (0 <= ny < h):
                continue
            if dist[ny][nx] != inf:
                continue

            dist[ny][nx] = dist[y][x] + 1
            q.append((ny, nx))

    ans = [["." for _ in range(w)] for _ in range(h)]

    for i in range(h):
        for j in range(w):
            if dist[i][j] % 2 == 1:
                continue

            ans[i][j] = "#"

    for ans_i in ans:
        print("".join(ans_i))


if __name__ == "__main__":
    main()
