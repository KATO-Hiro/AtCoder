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

    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    acc = [0] * n

    for i in range(1, n):
        if i % 2 == 1:
            acc[i] = acc[i - 1]
        else:
            acc[i] = acc[i - 1] + a[i] - a[i - 1]

    def f(x):
        i, value = bisect_ge(a, x)

        if i % 2 == 1:
            result = acc[i]
        else:
            result = acc[i] - (value - x)

        return result

    for _ in range(q):
        li, ri = map(int, input().split())
        print(f(ri) - f(li))


if __name__ == "__main__":
    main()
