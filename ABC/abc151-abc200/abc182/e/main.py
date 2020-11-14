# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    h, w, n, m = map(int, input().split())
    # -1: Block
    #  0: Not used
    #  1: On
    lights1 = [[0 for _ in range(w)] for _ in range(h)]
    lights2 = [[0 for _ in range(w)] for _ in range(h)]

    for i in range(n):
        ai, bi = map(int, input().split())
        ai -= 1
        bi -= 1
        lights1[ai][bi] = 1
        lights2[ai][bi] = 1

    for j in range(m):
        ci, di = map(int, input().split())
        ci -= 1
        di -= 1
        lights1[ci][di] = -1
        lights2[ci][di] = -1

    # Right
    for i in range(h):
        for j in range(1, w):
            if lights1[i][j - 1] == 1 and lights1[i][j] == 0:
                lights1[i][j] = 1

    # Left
    for i in range(h):
        for j in range(w - 2, -1, -1):
            if lights1[i][j + 1] == 1 and lights1[i][j] == 0:
                lights1[i][j] = 1

    # Down
    for j in range(w):
        for i in range(1, h):
            if lights2[i - 1][j] == 1 and lights2[i][j] == 0:
                lights2[i][j] = 1

    # Up
    for j in range(w):
        for i in range(h - 2, -1, -1):
            if lights2[i + 1][j] == 1 and lights2[i][j] == 0:
                lights2[i][j] = 1

    ans = 0

    for i in range(h):
        for j in range(w):
            if lights1[i][j] == 1 or lights2[i][j] == 1:
                ans += 1

    print(ans)


if __name__ == "__main__":
    main()
