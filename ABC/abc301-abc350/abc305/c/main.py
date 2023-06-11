# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    h, w = map(int, input().split())
    s = [list(input().rstrip()) for _ in range(h)]
    hi = set()
    wj = set()

    for i in range(h):
        for j in range(w):
            if s[i][j] == "#":
                hi.add(i)
                wj.add(j)

    h_min, h_max, w_min, w_max = min(hi), max(hi), min(wj), max(wj)

    for i in range(h_min, h_max + 1):
        for j in range(w_min, w_max + 1):
            if s[i][j] == ".":
                print(i + 1, j + 1)
                exit()


if __name__ == "__main__":
    main()
