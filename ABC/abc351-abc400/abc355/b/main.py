# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import pairwise

    input = sys.stdin.readline

    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = []

    for ai in a:
        c.append((ai, 0))

    for bj in b:
        c.append((bj, 1))

    c.sort()

    for (ci, i), (cj, j) in pairwise(c):
        if i == j == 0:
            print("Yes")
            exit()

    print("No")


if __name__ == "__main__":
    main()
