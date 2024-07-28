# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    h, w = map(int, input().split())
    si, sj = map(int, input().split())
    si -= 1
    sj -= 1
    s = [list(input().rstrip()) for _ in range(h)]
    x = input().rstrip()
    pos_y, pos_x = si, sj

    for xi in x:
        nx = pos_x
        ny = pos_y

        if xi == "L":
            nx -= 1
        elif xi == "R":
            nx += 1
        elif xi == "U":
            ny -= 1
        else:
            ny += 1

        if not (0 <= ny < h):
            continue
        if not (0 <= nx < w):
            continue
        if s[ny][nx] == "#":
            continue

        pos_x = nx
        pos_y = ny

    print(pos_y + 1, pos_x + 1)


if __name__ == "__main__":
    main()
