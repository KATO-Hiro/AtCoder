# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    h, w, n, m = map(int, input().split())
    # -1: Block
    #  0: Not used
    #  1: On
    grid = [[0 for _ in range(w)] for _ in range(h)]
    results = [[0 for _ in range(w)] for _ in range(h)]

    # See:
    # https://atcoder.jp/contests/abc182/submissions/17966314
    for i in range(n):
        ai, bi = map(int, input().split())
        ai -= 1
        bi -= 1
        grid[ai][bi] = 1

    for j in range(m):
        ci, di = map(int, input().split())
        ci -= 1
        di -= 1
        grid[ci][di] = -1

    # Right
    for i in range(h):
        # フラグの用意
        on = 0

        for j in range(w):
            # 光源かブロックか判定して、フラグを変更
            if grid[i][j] == 1:
                on = 1
            elif grid[i][j] == -1:
                on = 0

            # 論理和(OR)
            results[i][j] |= on

    # Left
    for i in range(h):
        on = 0

        for j in range(w - 1, -1, -1):
            if grid[i][j] == 1:
                on = 1
            elif grid[i][j] == -1:
                on = 0

            results[i][j] |= on

    # Down
    for j in range(w):
        on = 0

        for i in range(h):
            if grid[i][j] == 1:
                on = 1
            elif grid[i][j] == -1:
                on = 0

            results[i][j] |= on

    # Up
    for j in range(w):
        on = 0

        for i in range(h - 1, -1, -1):
            if grid[i][j] == 1:
                on = 1
            elif grid[i][j] == -1:
                on = 0

            results[i][j] |= on

    ans = 0

    for i in range(h):
        for j in range(w):
            ans += results[i][j]

    print(ans)


if __name__ == "__main__":
    main()
