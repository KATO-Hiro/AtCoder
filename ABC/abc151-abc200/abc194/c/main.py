# -*- coding: utf-8 -*-


def main():
    from itertools import accumulate

    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    a_2 = [ai ** 2 for ai in a]
    a_2_sum = list(accumulate(a_2))
    a_sum = list(accumulate(a))
    ans = 0

    for i in range(1, n):
        j = i - 1

        ans += a_2_sum[n - 1] - a_2_sum[i - 1]
        ans -= (a_sum[n - 1] - a_sum[i - 1]) * 2 * a[j]
        ans += (a[j] ** 2) * (n - i)

    print(ans)


if __name__ == "__main__":
    main()
