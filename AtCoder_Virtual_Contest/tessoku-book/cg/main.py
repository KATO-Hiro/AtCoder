# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    size = 1505
    grid = [[0 for _ in range(size)] for _ in range(size)]

    for _ in range(n):
        xi, yi = map(int, input().split())
        grid[yi][xi] += 1

    for i in range(size):
        for j in range(size):
            if j + 1 >= size:
                continue

            grid[i][j + 1] += grid[i][j]

    for j in range(size):
        for i in range(size):
            if i + 1 >= size:
                continue

            grid[i + 1][j] += grid[i][j]

    q = int(input())

    for _ in range(q):
        ai, bi, ci, di = map(int, input().split())

        summed = grid[di][ci]

        if ai - 1 >= 0:
            summed -= grid[di][ai - 1]
        if bi - 1 >= 0:
            summed -= grid[bi - 1][ci]
        if ai - 1 >= 0 and ai - 1 >= 0:
            summed += grid[bi - 1][ai - 1]

        print(summed)


if __name__ == "__main__":
    main()
