# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    k, g, m = map(int, input().split())
    glass = 0
    mug = 0

    for _ in range(k):
        if glass == g:
            glass = 0
        elif mug == 0:
            mug = m
        else:
            diff = g - glass

            if diff <= mug:
                mug -= diff
                glass = g
            else:
                glass += mug
                mug = 0

    print(glass, mug)


if __name__ == "__main__":
    main()
