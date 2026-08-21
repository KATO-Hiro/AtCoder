# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import accumulate

    input = sys.stdin.readline

    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    acc = list(accumulate(a, initial=0))

    for _ in range(m):
        li, ri, ki = map(int, input().split())

        if acc[ri] - acc[li - 1] >= ki:
            print("Dangerous")
        else:
            print("Safe")


if __name__ == "__main__":
    main()
