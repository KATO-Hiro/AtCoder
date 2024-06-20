# -*- coding: utf-8 -*-


def ceil(a, b):
    return (a + b - 1) // b


def main():
    import sys
    from itertools import pairwise

    input = sys.stdin.readline

    n, l, w = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0

    for ai, aj in pairwise(a):
        diff = aj - ai
        ans += max(0, ceil(diff, w) - 1)

    if a[0] != 0:
        ans += ceil(a[0], w)
    if a[-1] != l:
        ans += ceil(l - (a[-1] + w), w)

    print(ans)


if __name__ == "__main__":
    main()
