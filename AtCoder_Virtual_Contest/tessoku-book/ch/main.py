# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    size = 1510
    grid = [[0 for _ in range(size)] for _ in range(size)]

    for _ in range(n):
        ai, bi, ci, di = map(int, input().split())
        grid[ai][bi] += 1
        grid[ci][bi] -= 1
        grid[ai][di] -= 1
        grid[ci][di] += 1

    for i in range(size):
        for j in range(size):
            if j + 1 >= size:
                continue

            grid[i][j + 1] += grid[i][j]

    for j in range(1501):
        for i in range(1501):
            if i + 1 >= size:
                continue

            grid[i + 1][j] += grid[i][j]

    ans = 0

    for i in range(size):
        for j in range(size):
            if grid[i][j] >= 1:
                ans += 1

    print(ans)


if __name__ == "__main__":
    main()
