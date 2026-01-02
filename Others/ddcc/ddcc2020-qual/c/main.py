# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    h, w, k = map(int, input().split())
    grid = [list(input().rstrip()) for _ in range(h)]
    pending = -1
    ans = [[pending] * w for _ in range(h)]
    id = 1

    for i in range(h):
        for j in range(w):
            if grid[i][j] == ".":
                continue

            ans[i][j] = id
            id += 1

    # 左から右へ
    for i in range(h):
        for j in range(1, w):
            if ans[i][j] != pending:
                continue

            ans[i][j] = ans[i][j - 1]

    # 右から左へ
    for i in range(h):
        for j in range(w - 2, -1, -1):
            if ans[i][j] != pending:
                continue

            ans[i][j] = ans[i][j + 1]

    # 上から下へ
    for j in range(w):
        for i in range(1, h):
            if ans[i][j] != pending:
                continue

            ans[i][j] = ans[i - 1][j]

    # 下から上へ
    for j in range(w):
        for i in range(h - 2, -1, -1):
            if ans[i][j] != pending:
                continue

            ans[i][j] = ans[i + 1][j]

    for ans_i in ans:
        print(*ans_i)


if __name__ == "__main__":
    main()
