# -*- coding: utf-8 -*-


from bisect import bisect_right


def bisect_le(sorted_array: list[int], value: int):
    """Find the largest element <= x and its index, or None if it doesn't exist."""

    if sorted_array[0] <= value:
        index: int = bisect_right(sorted_array, value) - 1

        return index, sorted_array[index]

    return None, None


def main():
    import sys
    from itertools import accumulate

    input = sys.stdin.readline

    n, m = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    b = [0] + sorted(list(map(int, input().split())))
    acc_b = list(accumulate(b))
    mod = 998244353
    ans = 0

    for ai in a:
        count, value = bisect_le(b, ai)  # the largest element <= x

        if count is None:
            continue

        ans += ai * count - acc_b[count]
        ans %= mod
        ans += (acc_b[m] - acc_b[count]) - ai * (m - count)
        ans %= mod

    print(ans)


if __name__ == "__main__":
    main()
