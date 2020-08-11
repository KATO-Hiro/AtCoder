# -*- coding: utf-8 -*-


def main():
    from itertools import accumulate
    from bisect import bisect_left

    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    summed_a = list(accumulate([0] + a))
    ans = 0

    for i in range(n + 1):
        index = bisect_left(summed_a, summed_a[i] + k)
        ans += n - index + 1

    print(ans)


if __name__ == '__main__':
    main()
