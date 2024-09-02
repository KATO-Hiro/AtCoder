# -*- coding: utf-8 -*-


def f(array):
    from itertools import pairwise

    if len(array) <= 1:
        return 0

    summed = 0

    for ai, aj in pairwise(array):
        summed += abs(aj - ai)

    return summed


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    left, right = [], []

    for _ in range(n):
        ai, si = input().rstrip().split()
        ai = int(ai)

        if si == "L":
            left.append(ai)
        else:
            right.append(ai)

    ans = f(left) + f(right)

    print(ans)


if __name__ == "__main__":
    main()
