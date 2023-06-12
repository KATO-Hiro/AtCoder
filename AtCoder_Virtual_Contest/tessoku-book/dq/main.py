# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]
    q = int(input())
    rows = [i for i in range(n)]

    for _ in range(q):
        qi, xi, yi = map(int, input().split())
        xi -= 1
        yi -= 1

        if qi == 1:
            # swap
            rows[xi], rows[yi] = rows[yi], rows[xi]
        else:
            print(a[rows[xi]][yi])


if __name__ == "__main__":
    main()
