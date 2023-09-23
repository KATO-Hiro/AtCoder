# -*- coding: utf-8 -*-


from bisect import bisect_left, bisect_right
from typing import List


def bisect_lt(sorted_array: List[int], value: int):
    """Find the largest element < x and its index, or None if it doesn't exist."""

    if sorted_array[0] < value:
        index: int = bisect_left(sorted_array, value) - 1

        return index, sorted_array[index]

    return None, None


def bisect_le(sorted_array: List[int], value: int):
    """Find the largest element <= x and its index, or None if it doesn't exist."""

    if sorted_array[0] <= value:
        index: int = bisect_right(sorted_array, value) - 1

        return index, sorted_array[index]

    return None, None


def bisect_gt(sorted_array: List[int], value: int):
    """Find the smallest element > x and its index, or None if it doesn't exist."""

    if sorted_array[-1] > value:
        index: int = bisect_right(sorted_array, value)

        return index, sorted_array[index]

    return None, None


def bisect_ge(sorted_array: List[int], value: int):
    """Find the smallest element >= x and its index, or None if it doesn't exist."""

    if sorted_array[-1] >= value:
        index: int = bisect_left(sorted_array, value)

        return index, sorted_array[index]

    return None, None


def main():
    import sys
    from itertools import accumulate

    input = sys.stdin.readline

    n, m, p = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    b = sorted(list(map(int, input().split())))
    acc_b = list(accumulate([0] + b + [0]))
    inf = 10**18
    c = [-inf] + b + [inf]
    ans = 0

    for ai in a:
        i, value = bisect_le(c, p - ai)  # the largest element <= x
        ans += acc_b[i] + ai * i
        ans += p * max(m - i, 0)

    print(ans)


if __name__ == "__main__":
    main()
