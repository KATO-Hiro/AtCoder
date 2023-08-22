# -*- coding: utf-8 -*-


from bisect import bisect_left, bisect_right
from typing import List


def bisect_le(sorted_array: List[int], value: int):
    """Find the largest element <= x and its index, or None if it doesn't exist."""

    if sorted_array[0] <= value:
        index: int = bisect_right(sorted_array, value) - 1

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
    a = [int(input()) for _ in range(n)]
    # ai = 2 ** x * y
    values = [0] * n
    counts = [0] * n

    for i, ai in enumerate(a):
        count = 0

        while ai % 2 == 0:
            ai //= 2
            count += 1

        # print(i, ai, count)
        counts[i] = 2**count
        values[i] = ai

    counts = list(accumulate(counts))
    # print(values)
    # print(counts)

    q = int(input())

    for _ in range(q):
        qi = int(input())
        i, value = bisect_ge(counts, qi)  # the smallest element >= x
        # print(i)
        print(values[i])


if __name__ == "__main__":
    main()
