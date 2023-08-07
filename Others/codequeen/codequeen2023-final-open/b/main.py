# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    grid = [["." for _ in range(n)] for _ in range(n)]
    original = set([i for i in range(n)])
    rows, cols = set(), set()

    for _ in range(n - 1):
        ri, ci = map(int, input().split())
        ri -= 1
        ci -= 1
        grid[ri][ci] = "#"

        rows.add(ri)
        cols.add(ci)

    # print(grid)
    # print(original - rows, original - cols)
    row = original - rows
    col = original - cols

    if len(row) != 1 or len(col) != 1:
        print(-1)
        exit()

    y, x = *row, *col
    dxy = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, -1), (-1, 1), (1, 1)]
    dxy = dxy[4:]
    ok = True

    for dx, dy in dxy:
        nx, ny = x, y
        # print(nx, ny)

        while 0 <= nx + dx < n and 0 <= ny + dy < n:
            nx += dx
            ny += dy

            if grid[ny][nx] == "#":
                ok = False
                break

    if ok:
        print(y + 1, x + 1)
    else:
        print(-1)


if __name__ == "__main__":
    main()
