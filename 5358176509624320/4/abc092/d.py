# -*- coding: utf-8 -*-


def main():
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    n = 100
    grid = [['.'] * n for _ in range(n // 2)]

    for _ in range(n // 2):
        grid.append(['#'] * n)

    print(n, n)

    for i in range(0, n // 2, 2):
        for j in range(0, n, 2):
            if b > 0:
                grid[i][j] = '#'
                b -= 1
            else:
                break

    for i in range(51, n, 2):
        for j in range(0, n, 2):
            if a > 0:
                grid[i][j] = '.'
                a -= 1
            else:
                break

    for g in grid:
        print(''.join(map(str, g)))


if __name__ == '__main__':
    main()
