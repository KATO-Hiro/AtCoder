# -*- coding: utf-8 -*-


def main():
    import sys

    sys.setrecursionlimit(10**8)

    input = sys.stdin.readline

    w = int(input())
    h = int(input())
    blocks = [list(map(int, input().split())) for _ in range(h)]
    dxy = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, -1), (-1, 1), (1, 1)]
    dxy = dxy[:4]

    # 引数に答え(移動できる回数)を持つ
    def dfs(i, j, depth):
        # 薄氷を通る = 便宜的に薄氷がなくなったとみなす
        blocks[i][j] = 0
        ans = 0

        for dx, dy in dxy:
            ny, nx = i + dy, j + dx

            if not (0 <= nx < w):
                continue
            if not (0 <= ny < h):
                continue
            if blocks[ny][nx] == 0:
                continue

            ans = max(ans, dfs(ny, nx, depth + 1))

        blocks[i][j] = 1  # 元に戻す

        return max(ans, depth + 1)

    ans = 0

    for i in range(h):
        for j in range(w):
            if blocks[i][j] == 0:
                continue

            ans = max(ans, dfs(i, j, 0))

    print(ans)


if __name__ == "__main__":
    main()
