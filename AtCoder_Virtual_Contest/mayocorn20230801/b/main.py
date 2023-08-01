# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import deque

    input = sys.stdin.readline

    h, w = map(int, input().split())
    # TODO: Change input format if needs.
    g = [list(input().rstrip()) for _ in range(h)]
    d = deque()
    d.append((0, 0))
    visited = [[False] * w for _ in range(h)]
    used = set()
    ans = list()

    while d:
        y, x = d.popleft()

        # print(y + 1, x + 1)

        if (y + 1, x + 1) in used:
            print(-1)
            exit()

        # if visited[y][x]:
        #     continue

        visited[y][x] = True

        used.add((y + 1, x + 1))
        ans.append((y + 1, x + 1))

        dy, dx = 0, 0

        if g[y][x] == "U":
            dy = -1
        elif g[y][x] == "D":
            dy = 1
        elif g[y][x] == "L":
            dx = -1
        elif g[y][x] == "R":
            dx = 1

        nx = x + dx
        ny = y + dy

        if nx < 0 or nx >= w or ny < 0 or ny >= h:
            continue
        # if visited[ny][nx]:
        #     continue

        d.append((ny, nx))

    # print(used)
    # print(ans)
    y, x = ans[-1]
    print(y, x)


if __name__ == "__main__":
    main()
