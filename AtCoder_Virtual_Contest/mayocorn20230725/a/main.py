# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = [list(input().rstrip()) for _ in range(n)]
    # print(a)
    b = [["" for _ in range(n)] for _ in range(n)]

    for j in range(n - 1):
        b[0][j + 1] = a[0][j]
        b[n - 1][j] = a[n - 1][j + 1]

    for i in range(n - 1):
        b[i][0] = a[i + 1][0]
        b[i + 1][n - 1] = a[i][n - 1]

    if n >= 3:
        for i in range(1, n - 1):
            for j in range(1, n - 1):
                b[i][j] = a[i][j]

    for bi in b:
        print("".join(bi))
    # print(b)


if __name__ == "__main__":
    main()
