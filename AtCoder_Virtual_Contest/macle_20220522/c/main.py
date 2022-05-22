# -*- coding: utf-8 -*-


# See:
# https://atcoder.jp/contests/hhkb2020/submissions/17301581
def count_cells(grids, h: int, w: int):
    dot = '.'
    up = [[1 if grids[i][j] == dot else 0 for j in range(w)] for i in range(h)]
    down = [[1 if grids[i][j] == dot else 0 for j in range(w)] for i in range(h)]
    left = [[1 if grids[i][j] == dot else 0 for j in range(w)] for i in range(h)]
    right = [[1 if grids[i][j] == dot else 0 for j in range(w)] for i in range(h)]
    
    for i in range(h - 2, -1, -1):
        for j in range(w):
            if (grids[i][j] == dot):
                up[i][j] = up[i + 1][j] + 1

    for i in range(1, h):
        for j in range(w):
            if (grids[i][j] == dot):
                down[i][j] = down[i - 1][j] + 1

    for i in range(h):
        for j in range(w - 2, -1, -1):
            if (grids[i][j] == dot):
                left[i][j] = left[i][j + 1] + 1

    for i in range(h):
        for j in range(1, w):
            if (grids[i][j] == dot):
                right[i][j] = right[i][j - 1] + 1

    ans = 0

    for i in range(h):
        for j in range(w):
            if grids[i][j] == dot:
                count = (up[i][j] + down[i][j] - 1) + (left[i][j] + right[i][j] - 1) - 1

                ans = max(ans, count)
    
    return ans


def main():
    import sys

    input = sys.stdin.readline

    h, w = map(int, input().split())
    # h rows * w columns.
    # values: '.' or '#'
    grids = [list(input().rstrip()) for _ in range(h)]  

    ans = count_cells(grids, h, w)
    print(ans)


if __name__ == "__main__":
    main()
