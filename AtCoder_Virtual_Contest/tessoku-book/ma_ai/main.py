# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import accumulate

    input = sys.stdin.readline

    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    b = [0] + list(accumulate(a))

    for _ in range(q):
        li, ri = map(int, input().split())
        print(b[ri] - b[li - 1])


if __name__ == "__main__":
    main()
