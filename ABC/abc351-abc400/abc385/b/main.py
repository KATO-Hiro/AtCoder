# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    h, w, y, x = map(int, input().split())
    y -= 1
    x -= 1
    s = [list(input().rstrip()) for _ in range(h)]
    t = input().rstrip()
    visited = [[False] * w for _ in range(h)]

    for ti in t:
        if s[y][x] == "#":
            continue

        if ti == "U" and 0 <= y - 1 < h and s[y - 1][x] != "#":
            y -= 1
        elif ti == "D" and 0 <= y + 1 < h and s[y + 1][x] != "#":
            y += 1
        elif ti == "L" and 0 <= x - 1 < w and s[y][x - 1] != "#":
            x -= 1
        elif ti == "R" and 0 <= x + 1 < w and s[y][x + 1] != "#":
            x += 1
        else:
            continue

        visited[y][x] = True

    count = 0

    for i in range(h):
        for j in range(w):
            if s[i][j] == "@" and visited[i][j]:
                count += 1

    print(y + 1, x + 1, count)


if __name__ == "__main__":
    main()
