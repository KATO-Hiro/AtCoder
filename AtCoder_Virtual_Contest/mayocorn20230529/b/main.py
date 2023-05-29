# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    b = [list(map(int, input().split())) for _ in range(n)]
    flag = True

    for i in range(n):
        for j in range(m):
            # 右側は+1
            if j + 1 < m and b[i][j] + 1 != b[i][j + 1]:
                flag = False
                break
            # 下側は+7
            if i + 1 < n and b[i][j] + 7 != b[i + 1][j]:
                flag = False
                break
            # 7の倍数は右端
            if b[i][j] % 7 == 0 and j != m - 1:
                flag = False
                break

    if flag:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
