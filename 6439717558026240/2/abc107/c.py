# -*- coding: utf-8 -*-


def main():
    from bisect import bisect
    from itertools import accumulate

    n, k = map(int, input().split())
    x = list(map(int, input().split()))
    summed_x = list(accumulate([0] + x))
    ans = float('inf')
    pos = bisect(x, 0)

    if min(x) * max(x) >= 0:
        if min(x) < 0:
            print(abs(x[::-1][k - 1]))
        else:
            print(x[k - 1])
    else:
        pass
        # for i in range(pos + 1):
        #     dist1 = 2 * () + abs()


if __name__ == '__main__':
    main()
