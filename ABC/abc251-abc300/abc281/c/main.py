# -*- coding: utf-8 -*-


def main():
    from itertools import accumulate
    from bisect import bisect
    import sys

    input = sys.stdin.readline

    n, t = map(int, input().split())
    a = list(map(int, input().split()))

    summed_a = sum(a)
    t %= summed_a
    b = list(accumulate([0] + a + [10 ** 10]))

    index = bisect(b, t)
    ti = t - b[index - 1]

    print(index, ti)
    

if __name__ == "__main__":
    main()
