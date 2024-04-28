# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = [list(input().rstrip()) for _ in range(n)]
    b = [list(input().rstrip()) for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if a[i][j] != b[i][j]:
                print(i + 1, j + 1)
                exit()


if __name__ == "__main__":
    main()
