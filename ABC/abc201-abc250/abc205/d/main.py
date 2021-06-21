# -*- coding: utf-8 -*-


def main():
    from bisect import bisect_left
    import sys

    input = sys.stdin.readline

    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    count = [ai - index for index, ai in enumerate(a, 1)]

    for _ in range(q):
        ki = int(input())

        r = bisect_left(count, ki)

        if r == 0:
            ans = ki
        else:
            ans = a[r - 1] + (ki - count[r - 1])

        print(ans)


if __name__ == "__main__":
    main()
