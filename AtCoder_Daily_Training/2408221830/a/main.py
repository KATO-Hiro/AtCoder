# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    t = input().rstrip()
    x, y = 0, 0
    dir = 0
    d = {0: (1, 0), 1: (0, -1), 2: (-1, 0), 3: (0, 1)}  # 東、南、西、北

    for ti in t:
        if ti == "S":
            dx, dy = d[dir]
            x += dx
            y += dy
        else:
            dir += 1
            dir %= 4

    print(x, y)


if __name__ == "__main__":
    main()
