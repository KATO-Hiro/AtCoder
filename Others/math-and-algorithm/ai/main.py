# -*- coding: utf-8 -*-


def main():
    from itertools import accumulate
    import sys

    input = sys.stdin.readline

    n, q = map(int, input().split())
    a = [0] + list(map(int, input().split()))
    b = list(accumulate(a))

    for _ in range(q):
        li, ri = map(int, input().split())
        print(b[ri] - b[li - 1])


if __name__ == "__main__":
    main()
