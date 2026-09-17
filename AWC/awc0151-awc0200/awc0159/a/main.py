# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m, k = map(int, input().split())
    grid = [["#" for _ in range(m)] for _ in range(n)]

    for _ in range(k):
        ri, ci = map(int, input().split())
        ri -= 1
        ci -= 1
        grid[ri][ci] = "."

    for g in grid:
        print("".join(g))


if __name__ == "__main__":
    main()
