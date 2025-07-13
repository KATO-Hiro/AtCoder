# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import pairwise

    input = sys.stdin.readline

    n, m = map(int, input().split())
    x = sorted(list(map(int, input().split())))
    d = [(xj - xi) for xi, xj in pairwise(x)]
    d.sort()

    print(sum(d[: n - m]))


if __name__ == "__main__":
    main()
