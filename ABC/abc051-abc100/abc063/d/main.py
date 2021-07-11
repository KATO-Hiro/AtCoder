# -*- coding: utf-8 -*-


def check(h, a, b, x):
    from math import ceil

    count = 0

    for hi in h:
        hi -= x * b

        if hi <= 0:
            continue

        count += ceil(hi / (a - b))
    
    return count <= x


def main():
    import sys

    input = sys.stdin.readline

    n, a, b = map(int, input().split())
    h = [int(input()) for _ in range(n)]

    ng = 0
    ok = 10 ** 9 + 1

    while ok - ng > 1:
        wj = (ok +  ng) // 2

        if check(h, a, b, wj):
            ok = wj
        else:
            ng = wj

    print(ok)


if __name__ == "__main__":
    main()

