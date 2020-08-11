# -*- coding: utf-8 -*-


def main():
    n = int(input())
    grid = [[True for _ in range(n)] for _ in range(n)]

    # KeyInsight
    # 補グラフ
    if n % 2 == 0:
        for i in range(n):
            grid[i][n - i - 1] = False
    else:
        for i in range(n):
            grid[i][n - i - 2] = False

    ans = list()

    for i in range(n):
        for j in range(i, n):
            if i != j and grid[i][j]:
                ans.append((i, j))

    print(len(ans))

    for ai, bi in ans:
        print(ai + 1, bi + 1)


if __name__ == '__main__':
    main()
