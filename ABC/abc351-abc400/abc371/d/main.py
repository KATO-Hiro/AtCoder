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


def main():
    import sys
    from itertools import accumulate

    input = sys.stdin.readline

    n = int(input())
    x = list(map(int, input().split()))
    p = list(map(int, input().split()))

    inf = 10**12
    x = [-inf] + x + [inf]
    p = [0] + p + [0]
    acc_p = list(accumulate(p))

    q = int(input())

    for _ in range(q):
        li, ri = map(int, input().split())

        j, _ = bisect_le(x, ri)  # the largest element <= ri
        i, _ = bisect_lt(x, li)  # the largest element < li
        print(acc_p[j] - acc_p[i])


if __name__ == "__main__":
    main()
