# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import pairwise

    input = sys.stdin.readline

    n = int(input())
    t = list(map(int, input().split()))
    candidates = []

    for ti, tj in pairwise(t):
        candidates.append(tj - ti)

    candidates.sort()
    print(candidates[0], candidates[-1])


if __name__ == "__main__":
    main()
