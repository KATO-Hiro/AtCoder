# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    h, w, n = map(int, input().split())
    grid = [[1 for _ in range(w)] for _ in range(h)]

    # 最大正方形問題
    # 穴のあるマスを0、穴のないマスを1
    for _ in range(n):
        ai, bi = map(int, input().split())
        ai -= 1
        bi -= 1
        grid[ai][bi] = 0

    # マス(i, j)よりも左上側にできる正方形の大きさ
    # See:
    # http://algorithms.blog55.fc2.com/blog-entry-131.html
    for i in range(1, h):
        for j in range(1, w):
            if grid[i][j] == 0:
                continue

            grid[i][j] = min(grid[i - 1][j], grid[i][j - 1], grid[i - 1][j - 1]) + 1

    ans = 0

    for i in range(h):
        for j in range(w):
            ans += grid[i][j]

    print(ans)


if __name__ == "__main__":
    main()
