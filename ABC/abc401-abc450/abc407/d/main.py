# -*- coding: utf-8 -*-


def main():
    import sys

    sys.setrecursionlimit(10**8)

    input = sys.stdin.readline

    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    xor_all = 0
    used = [[False] * w for _ in range(h)]
    dominos = list()
    ans = 0

    for i in range(h):
        for j in range(w):
            xor_all ^= a[i][j]

    def dfs(row, col):
        if row >= h:
            candidate = xor_all

            for r1, c1, r2, c2 in dominos:
                candidate ^= a[r1][c1]
                candidate ^= a[r2][c2]

            nonlocal ans
            ans = max(ans, candidate)

            return

        # 次のマスに進む
        nr, nc = row, col + 1

        if nc >= w:
            nr, nc = nr + 1, 0

        # 既に訪問済みなら次のマスに進む
        if used[row][col]:
            dfs(nr, nc)
            return

        # 現在のマスを選択しない
        dfs(nr, nc)

        # 1 * 2 のマスを置く
        if (col + 1 < w) and not used[row][col + 1]:
            used[row][col] = used[row][col + 1] = True
            dominos.append((row, col, row, col + 1))
            dfs(nr, nc)
            dominos.pop()
            used[row][col] = used[row][col + 1] = False

        # 2 * 1 のマスを置く
        if (row + 1 < h) and not used[row + 1][col]:
            used[row][col] = used[row + 1][col] = True
            dominos.append((row, col, row + 1, col))
            dfs(nr, nc)
            dominos.pop()
            used[row][col] = used[row + 1][col] = False

    dfs(0, 0)
    print(ans)


if __name__ == "__main__":
    main()
