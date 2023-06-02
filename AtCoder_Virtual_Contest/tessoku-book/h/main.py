# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    h, w = map(int, input().split())
    x = [list(map(int, input().split())) for _ in range(h)]
    q = int(input())

    for i in range(h):
        for j in range(w):
            if j + 1 >= w:
                continue

            x[i][j + 1] += x[i][j]

    for j in range(w):
        for i in range(h):
            if i + 1 >= h:
                continue

            x[i + 1][j] += x[i][j]

    for _ in range(q):
        ai, bi, ci, di = map(int, input().split())
        ai -= 1
        bi -= 1
        ci -= 1
        di -= 1

        summed = x[ci][di]

        if bi - 1 >= 0:
            summed -= x[ci][bi - 1]
        if ai - 1 >= 0:
            summed -= x[ai - 1][di]
        if bi - 1 >= 0 and ai - 1 >= 0:
            summed += x[ai - 1][bi - 1]

        print(summed)


if __name__ == "__main__":
    main()
