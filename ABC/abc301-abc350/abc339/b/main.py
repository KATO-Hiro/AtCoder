# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    h, w, n = map(int, input().split())
    s = [["." for _ in range(w)] for _ in range(h)]
    # print(s)
    i, j, dir = 0, 0, 0
    dxy = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    for _ in range(n):
        if s[i][j] == ".":
            s[i][j] = "#"

            dir += 1
        else:
            s[i][j] = "."
            dir -= 1

        dir %= 4

        dy, dx = dxy[dir]
        i += dy
        j += dx

        if i == h:
            i = 0
        if i == -1:
            i = h - 1
        if j == w:
            j = 0
        if j == -1:
            j = w - 1

    for si in s:
        print("".join(si))


if __name__ == "__main__":
    main()
