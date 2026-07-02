# -*- coding: utf-8 -*-


# See:
# https://kazun-kyopro.hatenablog.com/entry/ABC/298/B
def rotate_90_degrees_to_right(array: list[list]):
    return [list(ai)[::-1] for ai in zip(*array)]


def f(grid):
    while grid and grid[-1].count("#") == 0:
        grid.pop()

    return grid


def main():
    import sys

    input = sys.stdin.readline

    h, w = map(int, input().split())
    c = [list(input().rstrip()) for _ in range(h)]

    for _ in range(4):
        c = f(c)
        c = rotate_90_degrees_to_right(c)

    for ci in c:
        print("".join(ci))


if __name__ == "__main__":
    main()
