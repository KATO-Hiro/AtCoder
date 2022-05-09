# -*- coding: utf-8 -*-


def main():
    from bisect import bisect_left
    import sys

    input = sys.stdin.readline

    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    c = [ai - index for index, ai in enumerate(a, 1)]

    for _ in range(q):
        ki = int(input())
        right = bisect_left(c, ki)

        if right == 0:
            print(ki)
        else:
            print(a[right - 1] + (ki - c[right - 1]))


if __name__ == "__main__":
    main()
