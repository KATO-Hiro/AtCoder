# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    b = list()
    b = [[0] * h for _ in range(w)]

    for i in range(h):
        for j in range(w):
            b[j][i] = a[i][j]

    for bi in b:
        print(*bi)


if __name__ == "__main__":
    main()
