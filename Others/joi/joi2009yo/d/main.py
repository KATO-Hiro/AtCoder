# -*- coding: utf-8 -*-

ans = 0


def main():
    import sys

    sys.setrecursionlimit(10**8)

    input = sys.stdin.readline

    w = int(input())
    h = int(input())
    blocks = [list(map(int, input().split())) for _ in range(h)]
    # print(blocks)
    dxy = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, -1), (-1, 1), (1, 1)]
    dxy = dxy[:4]

    # 引数に答え(移動できる回数)を持つ
    def dfs(i, j, depth):
        global ans

        # 薄氷を通る = 便宜的に薄氷がなくなったとみなす
        blocks[i][j] = 0

        for dx, dy in dxy:
            ny, nx = i + dy, j + dx

            if not (0 <= nx < w):
                continue
            if not (0 <= ny < h):
                continue
            if blocks[ny][nx] == 0:
                continue

            dfs(ny, nx, depth + 1)

        blocks[i][j] = 1  # 元に戻す

        # 4方向に薄氷があるか?
        ice_count = 0

        for dx, dy in dxy:
            ny, nx = i + dy, j + dx

            if not (0 <= nx < w):
                continue
            if not (0 <= ny < h):
                continue
            if blocks[ny][nx] == 1:
                ice_count += 1

        if ice_count == 0:
            ans = max(ans, depth + 1)
            return ans

    for i in range(h):
        for j in range(w):
            if blocks[i][j] == 0:
                continue

            dfs(i, j, 0)

    print(ans)


if __name__ == "__main__":
    main()
