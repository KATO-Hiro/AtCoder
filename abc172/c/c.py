# -*- coding: utf-8 -*-


def main():
    from bisect import bisect
    from itertools import accumulate

    import sys
    input = sys.stdin.readline

    n, m, k = map(int, input().split())
    a = list(accumulate([0] + list(map(int, input().split()))))
    b = list(accumulate([0] + list(map(int, input().split()))))

    i1 = bisect(a, k) - 1
    j1 = bisect(b, max(0, k - a[i1])) - 1
    i2 = bisect(b, k) - 1
    j2 = bisect(a, max(0, k - b[i2])) - 1

    print(max(i1 + j1, i2 + j2))


if __name__ == '__main__':
    main()
