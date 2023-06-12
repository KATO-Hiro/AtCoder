# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    h, w, n = map(int, input().split())
    z = [[0 for _ in range(w + 1)] for _ in range(h + 1)]

    for _ in range(n):
        ai, bi, ci, di = map(int, input().split())
        ai -= 1
        bi -= 1

        z[ai][bi] += 1
        z[ci][bi] -= 1
        z[ai][di] -= 1
        z[ci][di] += 1

    for j in range(w - 1):
        for i in range(h):
            z[i][j + 1] += z[i][j]

    for i in range(h - 1):
        for j in range(w):
            z[i + 1][j] += z[i][j]

    for i in range(h):
        print(*z[i][:-1])


if __name__ == "__main__":
    main()
