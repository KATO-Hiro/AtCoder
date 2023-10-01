# -*- coding: utf-8 -*-


from copy import deepcopy
from typing import List


# See:
# https://kazun-kyopro.hatenablog.com/entry/ABC/298/B
def rotate_90_degrees_to_right(array: List[List]):
    new_array = [list(ai)[::-1] for ai in zip(*array)]

    return new_array


def main():
    import sys

    sys.setrecursionlimit(10**8)

    input = sys.stdin.readline

    n = 3
    size = 4
    polyominos = list()

    for _ in range(n):
        pi = [list(input().rstrip()) for _ in range(size)]
        polyominos.append(pi)

    rotate_count = 3

    h, w = 4, 4

    # ポリオミノをシフトさせて配置できるか?
    def can_put_polyomino(grid, polyomino, dy, dx):
        for y, pi in enumerate(polyomino):
            for x, pij in enumerate(pi):
                if pij != "#":
                    continue

                ny, nx = y + dy, x + dx

                if not (0 <= nx < w):
                    return False
                if not (0 <= ny < h):
                    return False
                if grid[ny][nx]:
                    return False

                grid[ny][nx] = True

        return True

    def dfs(i, grid, ps):
        if i == rotate_count:
            ok = True

            for y in range(size):
                for x in range(size):
                    if not grid[y][x]:
                        ok = False
                        break

            if ok:
                print("Yes")
                exit()

            return

        for dy in range(-size + 1, size):
            for dx in range(-size + 1, size):
                grid2 = deepcopy(grid)
                flag = can_put_polyomino(grid2, ps[i], dy, dx)

                if flag:
                    dfs(i + 1, grid2, ps)

    # 1番目を固定して、2番目・3番目を回転させる
    # 正方形なので、1番目は回転が不要
    for second in range(rotate_count + 1):
        for third in range(rotate_count + 1):
            dfs(0, [[False for _ in range(size)] for _ in range(size)], polyominos)
            polyominos[2] = rotate_90_degrees_to_right(deepcopy(polyominos[2]))

        polyominos[1] = rotate_90_degrees_to_right(deepcopy(polyominos[1]))

    print("No")


if __name__ == "__main__":
    main()
