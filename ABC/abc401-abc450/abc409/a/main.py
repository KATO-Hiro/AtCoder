# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import pairwise

    input = sys.stdin.readline

    n, s = map(int, input().split())
    t = [0] + list(map(int, input().split()))

    for ti, tj in pairwise(t):
        diff = tj - ti

        if diff > s:
            print("No")
            exit()

    print("Yes")


if __name__ == "__main__":
    main()
