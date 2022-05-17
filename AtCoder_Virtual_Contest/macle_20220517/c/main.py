# -*- coding: utf-8 -*-


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
            elif (grids[i][j] == ""):
                up[i][j] = up[i + 1][j]

    for i in range(1, h):
        for j in range(w):
            if (grids[i][j] == dot):
                down[i][j] = down[i - 1][j] + 1
            elif (grids[i][j] == ""):
                down[i][j] = down[i - 1][j]

    for i in range(h):
        for j in range(w - 2, -1, -1):
            if (grids[i][j] == dot):
                left[i][j] = left[i][j + 1] + 1
            elif (grids[i][j] == ""):
                left[i][j] = left[i][j + 1]

    for i in range(h):
        for j in range(1, w):
            if (grids[i][j] == dot):
                right[i][j] = right[i][j - 1] + 1
            elif (grids[i][j] == ""):
                right[i][j] = right[i][j - 1]

    ans = 0

    for i in range(h):
        for j in range(w):
            if grids[i][j] != "#":
                if up[i][j] > 0 or down[i][j] > 0 or left[i][j] > 0 or right[i][j] > 0:
                    ans += 1
    
    return ans




def main():
    import sys

    input = sys.stdin.readline

    h, w, n, m = map(int, input().split())
    # h rows * w columns.
    # values: '.' or '#'
    grids = [[""] * w for _ in range(h)]  

    for i in range(n):
        ai, bi = map(int, input().split())
        ai -= 1
        bi -= 1
        grids[ai][bi] = "."

    for i in range(m):
        ci, di = map(int, input().split())
        ci -= 1
        di -= 1
        grids[ci][di] = "#"

    ans = count_cells(grids, h, w)
    print(ans)


if __name__ == "__main__":
    main()
