# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import deque
    from copy import deepcopy

    input = sys.stdin.readline

    n, m = map(int, input().split())
    # TODO: Change input format if needs.
    s = [list(input().rstrip()) for _ in range(n)]
    d = deque()
    d.append((1, 1))
    visited = [[False] * m for _ in range(n)]
    # dist = [[0] * m for _ in range(n)]
    # dist[0][0] = 1  # Initialize
    dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    used = set()
    used.add((1, 1))

    while d:
        y, x = d.popleft()

        # if visited[y][x]:
        #     continue

        visited[y][x] = True

        for dx, dy in dxy:
            nx, ny = deepcopy(x), deepcopy(y)

            while True:
                nx += dx
                ny += dy

                if nx < 0 or nx >= m or ny < 0 or ny >= n:
                    continue
                if visited[ny][nx]:
                    continue
                if s[ny][nx] == "#":
                    break
                    # continue

                visited[ny][nx] = True

            if (ny - dy, nx - dx) not in used:
                # print(y, x, ny, nx, ny - dy, nx - dx)
                used.add((ny - dy, nx - dx))
                d.append((ny - dy, nx - dx))
                visited[ny - dy][nx - dx] = False

    ans = 0

    for i in range(n):
        for j in range(m):
            if visited[i][j]:
                ans += 1

    print(ans)


if __name__ == "__main__":
    main()
