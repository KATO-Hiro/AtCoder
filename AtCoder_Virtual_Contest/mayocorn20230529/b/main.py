# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    b = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(n)]
    base = b[0][0]

    p, q = divmod(base, 7)

    if (q + m - 1) >= 7:
        print("No")
        exit()

    for i in range(n):
        for j in range(m):
            if b[i][j] != base + (i * 7 + j):
                print("No")
                exit()

    print("Yes")


if __name__ == "__main__":
    main()
