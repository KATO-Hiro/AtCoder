# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    ok = [[False] * n for _ in range(n)]

    for _ in range(m):
        k, *x = map(int, input().split())

        for i in range(k):
            for j in range(i + 1, k):
                ok[x[i] - 1][x[j] - 1] = True
                ok[x[j] - 1][x[i] - 1] = True

    for i in range(n):
        for j in range(i + 1, n):
            if not ok[i][j]:
                print("No")
                exit()

    print("Yes")


if __name__ == "__main__":
    main()
