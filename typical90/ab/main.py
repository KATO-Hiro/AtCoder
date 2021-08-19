# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    size_max = 1010
    size = 1000
    grid = [[0] * size_max for _ in range(size_max)]
    ans = [0] * (n + 1)

    for _ in range(n):
        lx, ly, rx, ry = map(int, input().split())
        grid[ly][lx] += 1
        grid[ry][rx] += 1
        grid[ry][lx] -= 1
        grid[ly][rx] -= 1
    
    for y in range(size):
        for x in range(size - 1):
            grid[y][x + 1] += grid[y][x]

    for y in range(size - 1):
        for x in range(size):
            grid[y + 1][x] += grid[y][x]
    
    for y in range(size):
        for x in range(size):
            count = grid[y][x]

            if  count >= 1:
                ans[count] += 1
    
    print('\n'.join(map(str, ans[1:])))


if __name__ == "__main__":
    main()
