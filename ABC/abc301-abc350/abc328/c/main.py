# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import accumulate

    input = sys.stdin.readline

    n, q = map(int, input().split())
    s = input().rstrip()
    t = [0] * (n + 10)

    for i, (si, sj) in enumerate(zip(s, s[1:]), 1):
        if si == sj:
            t[i] = 1

    t = list(accumulate(t, initial=0))
    # print(t)

    for _ in range(q):
        li, ri = map(int, input().split())
        print(t[ri] - t[li])


if __name__ == "__main__":
    main()
