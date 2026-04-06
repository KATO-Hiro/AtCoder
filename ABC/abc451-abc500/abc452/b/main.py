# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    h, w = map(int, input().split())
    s = [["."] * w for _ in range(h)]

    for i in [0, h - 1]:
        for j in range(w):
            s[i][j] = "#"

    for j in [0, w - 1]:
        for i in range(h):
            s[i][j] = "#"

    for si in s:
        print("".join(si))


if __name__ == "__main__":
    main()
