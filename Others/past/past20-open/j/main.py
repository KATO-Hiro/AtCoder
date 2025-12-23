# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import deque

    input = sys.stdin.readline

    n = int(input())
    s = [list(input().rstrip()) for _ in range(n)]
    dxy = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, -1), (-1, 1), (1, 1)]
    dxy = dxy[:4]
    counts = [[0] * n for _ in range(n)]
    q = deque()

    for y in range(n):
        for x in range(n):
            if s[y][x] == "#":
                continue

            count = 0

            for dx, dy in dxy:
                ny, nx = y + dy, x + dx

                if not (0 <= ny < n):
                    continue
                if not (0 <= nx < n):
                    continue
                if s[ny][nx] == ".":
                    continue

                count += 1

            counts[y][x] = count

            if counts[y][x] <= 2:
                continue

            q.append((y, x))

    used = set()
    ans = 0

    while q:
        y, x = q.popleft()

        if (y, x) in used:
            continue

        used.add((y, x))
        s[y][x] = "#"
        counts[y][x] = 0
        ans += 1

        for dx, dy in dxy:
            ny, nx = y + dy, x + dx

            if not (0 <= ny < n):
                continue
            if not (0 <= nx < n):
                continue
            if s[ny][nx] == "#":
                continue
            if (ny, nx) in used:
                continue

            count = 0

            for dx2, dy2 in dxy:
                ny2, nx2 = ny + dy2, nx + dx2

                if not (0 <= ny2 < n):
                    continue
                if not (0 <= nx2 < n):
                    continue
                if s[ny2][nx2] == ".":
                    continue

                count += 1

            counts[ny][nx] = count

            if count <= 2:
                continue

            q.append((ny, nx))

    print(ans)


if __name__ == "__main__":
    main()
