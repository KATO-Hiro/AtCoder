# -*- coding: utf-8 -*-


def main():
    from bisect import bisect
    from itertools import accumulate

    n, x = map(int, input().split())
    a = sorted([0] + list(map(int, input().split())))
    summed_a = list(accumulate(a))
    count = bisect(summed_a, x)

    if count >= n + 1:
        count -= 1

    if summed_a[count] == x:
        print(count)
    else:
        print(count - 1)


if __name__ == '__main__':
    main()
