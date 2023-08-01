# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    h, w, n = map(int, input().split())
    grids = [[1 for _ in range(w)] for _ in range(h)]

    for _ in range(n):
        ai, bi = map(int, input().split())
        ai -= 1
        bi -= 1
        grids[ai][bi] = 0

    # print(grids)
    for i in range(1, h):
        for j in range(1, w):
            if grids[i][j] == 0:
                continue

            grids[i][j] = min(grids[i - 1][j], grids[i][j - 1], grids[i - 1][j - 1]) + 1

    ans = 0

    for i in range(h):
        for j in range(w):
            ans += grids[i][j]

    print(ans)


if __name__ == "__main__":
    main()
