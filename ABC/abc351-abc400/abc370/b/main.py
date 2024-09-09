# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]
    i = 0

    for j in range(n):
        if j <= i:
            i = a[i][j] - 1
        else:
            i = a[j][i] - 1

    print(i + 1)


if __name__ == "__main__":
    main()
