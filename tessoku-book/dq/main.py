# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]
    q = int(input())
    rows = [i for i in range(n)]

    for i in range(q):
        qi, x, y = list(map(int, input().split()))
        x -= 1
        y -= 1

        if qi == 1:
            rows[x], rows[y] = rows[y], rows[x] 
        else:
            print(a[rows[x]][y])


if __name__ == "__main__":
    main()
