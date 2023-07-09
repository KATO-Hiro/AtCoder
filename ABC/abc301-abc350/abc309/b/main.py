# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = [list(input().rstrip()) for _ in range(n)]
    b = [["" for _ in range(n)] for _ in range(n)]

    for j in range(1, n):
        b[0][j] = a[0][j - 1]
        b[n - 1][j - 1] = a[n - 1][j]

    for i in range(1, n):
        b[i - 1][0] = a[i][0]
        b[i][n - 1] = a[i - 1][n - 1]

    if n >= 3:
        for i in range(1, n - 1):
            for j in range(1, n - 1):
                b[i][j] = a[i][j]

    for bi in b:
        print("".join(bi))


if __name__ == "__main__":
    main()
