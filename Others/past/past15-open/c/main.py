# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    y, x, r, n = map(int, input().split())
    y += n
    x += n
    r2 = r**2
    size = 2 * n + 1
    s = [["." for _ in range(size)] for _ in range(size)]
    s[y][x] = "#"

    for i in range(size):
        for j in range(size):
            if (y - i) ** 2 + (x - j) ** 2 <= r2:
                s[i][j] = "#"

    for si in s:
        print(" ".join(si))


if __name__ == "__main__":
    main()
