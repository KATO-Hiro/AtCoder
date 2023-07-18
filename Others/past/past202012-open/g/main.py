# -*- coding: utf-8 -*-


def main():
    import sys

    sys.setrecursionlimit(10**8)

    input = sys.stdin.readline

    h, w = map(int, input().split())
    s = [list(input().rstrip()) for _ in range(h)]
    dxy = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, -1), (-1, 1), (1, 1)]
    dxy = set(dxy[:4])
    k = sum([si.count("#") for si in s])
    visited = [[False for _ in range(w)] for _ in range(h)]

    print(k)

    def dfs(y, x, path):
        if len(path) == k:
            for xi, yi in path:
                print(xi, yi)

            exit()

        if visited[y][x]:
            return

        visited[y][x] = True

        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy

            if not (0 <= nx < w):
                continue
            if not (0 <= ny < h):
                continue
            if s[ny][nx] == ".":
                continue
            if visited[ny][nx]:
                continue

            path.append((ny + 1, nx + 1))
            dfs(ny, nx, path)
            path.pop()
            # ここで訪問済みの状態を解除すると思い込んでいた。
            # visited[ny][nx] = False

        # 訪問済みの状態をここで解除する。対称性を意識すると良いのかも。
        visited[y][x] = False

    # 始点を決めて、DFS
    for i in range(h):
        for j in range(w):
            if s[i][j] == ".":
                continue

            dfs(i, j, [(i + 1, j + 1)])


if __name__ == "__main__":
    main()
