# -*- coding: utf-8 -*-


def main():
    import sys

    sys.setrecursionlimit(10**8)

    input = sys.stdin.readline

    h, w, k = map(int, input().split())
    s = [list(input().rstrip()) for _ in range(h)]
    dxy = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, -1), (-1, 1), (1, 1)]
    dxy = dxy[:4]
    ans = 0

    def dfs(y, x, count=0):
        if count == k:
            nonlocal ans
            ans += 1
            return

        used[y][x] = True

        for dx, dy in dxy:
            ny, nx = y + dy, x + dx

            if not (0 <= ny < h):
                continue
            if not (0 <= nx < w):
                continue
            if s[ny][nx] == "#":
                continue
            if used[ny][nx]:
                continue

            dfs(ny, nx, count + 1)

        used[y][x] = False

    used = [[False for _ in range(w)] for _ in range(h)]

    for i in range(h):
        for j in range(w):
            if s[i][j] == "#":
                continue

            dfs(i, j)

    print(ans)


if __name__ == "__main__":
    main()
