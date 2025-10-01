# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import deque

    input = sys.stdin.readline

    h, w = map(int, input().split())
    s = [list(input().rstrip()) for _ in range(h)]

    q = deque()
    inf = 10**18
    dist = [[inf for _ in range(w)] for _ in range(h)]

    for i in range(h):
        for j in range(w):
            if s[i][j] == ".":
                continue

            q.append((i, j))
            dist[i][j] = 0

    dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while q:
        y, x = q.popleft()
        di = dist[y][x]

        for dx, dy in dxy:
            ny, nx = y + dy, x + dx

            if not (0 <= ny < h):
                continue
            if not (0 <= nx < w):
                continue
            if dist[ny][nx] != inf:
                continue

            count = 0

            for dx2, dy2 in dxy:
                ny2, nx2 = ny + dy2, nx + dx2

                if not (0 <= ny2 < h):
                    continue
                if not (0 <= nx2 < w):
                    continue
                if dist[ny2][nx2] <= di:
                    count += 1
                    continue

            if count == 1:
                q.append((ny, nx))
                dist[ny][nx] = dist[y][x] + 1

    ans = 0

    for i in range(h):
        for j in range(w):
            if dist[i][j] != inf:
                ans += 1

    print(ans)


if __name__ == "__main__":
    main()
