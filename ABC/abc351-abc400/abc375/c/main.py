# -*- coding: utf-8 -*-

from typing import List


# See:
# https://kazun-kyopro.hatenablog.com/entry/ABC/298/B
def rotate_90_degrees_to_right(array: List[List]):
    return [list(ai)[::-1] for ai in zip(*array)]


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = [list(input().rstrip()) for _ in range(n)]

    # 90度回転は4種類しかない
    s90 = rotate_90_degrees_to_right(s[:])
    s180 = rotate_90_degrees_to_right(s90[:])
    s270 = rotate_90_degrees_to_right(s180[:])
    ans = [[""] * n for _ in range(n)]

    def write(k, grid):
        for j in range(k, n - k):
            ans[k][j] = grid[k][j]
            ans[n - k - 1][j] = grid[n - k - 1][j]
            ans[j][k] = grid[j][k]
            ans[j][n - k - 1] = grid[j][n - k - 1]

    for i in range(1, n // 2 + 1):
        i2 = i - 1

        if i % 4 == 1:
            write(i2, s90)
        elif i % 4 == 2:
            write(i2, s180)
        elif i % 4 == 3:
            write(i2, s270)
        else:
            write(i2, s)

    for ans_i in ans:
        print("".join(ans_i))


if __name__ == "__main__":
    main()
