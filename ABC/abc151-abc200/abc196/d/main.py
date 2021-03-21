# -*- coding: utf-8 -*-
from functools import lru_cache


@lru_cache(maxsize=None)
def main():
    import sys

    input = sys.stdin.readline
    sys.setrecursionlimit(10 ** 7)

    h, w, a, b = map(int, input().split())
    used = [[False for _ in range(w)] for _ in range(h)]

    def dfs(i, j, a, b):
        if a < 0 or b < 0:
            return 0
        if j == w:
            j = 0
            i += 1
        if i == h:
            return 1
        if used[i][j]:
            return dfs(i, j + 1, a, b)

        count = 0
        used[i][j] = True

        # 1マス
        count += dfs(i, j + 1, a, b - 1)

        # 2マス: 横方向
        if (j + 1) < w and not used[i][j + 1]:
            used[i][j + 1] = True
            count += dfs(i, j + 1, a - 1, b)
            used[i][j + 1] = False

        # 2マス: 縦方向
        if (i + 1) < h and not used[i + 1][j]:
            used[i + 1][j] = True
            count += dfs(i, j + 1, a - 1, b)
            used[i + 1][j] = False

        used[i][j] = False

        return count

    ans = dfs(0, 0, a, b)
    print(ans)


if __name__ == "__main__":
    main()
