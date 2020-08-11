# -*- coding: utf-8 -*-


def main():
    h, w = map(int, input().split())
    grids = [list(input()) for _ in range(h)]
    up = [[1 for __ in range(w)] for _ in range(h)]
    down = [[1 for __ in range(w)] for _ in range(h)]
    left = [[1 for __ in range(w)] for _ in range(h)]
    right = [[1 for __ in range(w)] for _ in range(h)]
    ans = 0

    for i in range(h - 1, -1, -1):
        for j in range(w):
            if (grids[i][j] == '.') and (i < h - 1):
                up[i][j] = up[i + 1][j] + 1
            elif grids[i][j] == '#':
                up[i][j] = 0

    for i in range(h):
        for j in range(w):
            if (grids[i][j] == '.') and (i > 0):
                down[i][j] = down[i - 1][j] + 1
            elif grids[i][j] == '#':
                down[i][j] = 0

    for i in range(h):
        for j in range(w - 1, -1, -1):
            if (grids[i][j] == '.') and (j < w - 1):
                left[i][j] = left[i][j + 1] + 1
            elif grids[i][j] == '#':
                left[i][j] = 0

    for i in range(h):
        for j in range(w):
            if (grids[i][j] == '.') and (j > 0):
                right[i][j] = right[i][j - 1] + 1
            elif grids[i][j] == '#':
                right[i][j] = 0

    for i in range(h):
        for j in range(w):
            ans = max(ans, (up[i][j] + down[i][j] - 1) + (left[i][j] + right[i][j] - 1) - 1)

    print(ans)


if __name__ == '__main__':
    main()
