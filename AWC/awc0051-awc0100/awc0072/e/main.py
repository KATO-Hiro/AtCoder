# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import accumulate

    input = sys.stdin.readline

    n, m = map(int, input().split())
    s = list(map(int, input().split()))
    p = list(map(int, input().split()))
    diff = []

    for si, pi in zip(s, p):
        di = si - pi

        if di >= 0:
            diff.append(1)
        else:
            diff.append(0)

    acc = list(accumulate(diff, initial=0))

    for _ in range(m):
        li, ri = map(int, input().split())

        if (acc[ri] - acc[li - 1]) == (ri - li + 1):
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    main()
