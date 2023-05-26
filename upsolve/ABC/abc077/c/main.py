# -*- coding: utf-8 -*-

from bisect import bisect_left, bisect_right
from typing import List


def bisect_lt(sorted_array: List[int], value: int):
    """Find the largest element < x and its index, or None if it doesn't exist."""

    if sorted_array[0] < value:
        index: int = bisect_left(sorted_array, value) - 1

        return index, sorted_array[index]

    return None, None


def bisect_gt(sorted_array: List[int], value: int):
    """Find the smallest element > x and its index, or None if it doesn't exist."""

    if sorted_array[-1] > value:
        index: int = bisect_right(sorted_array, value)

        return index, sorted_array[index]

    return None, None


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = sorted(list(map(int, input().split())))
    b = sorted(list(map(int, input().split())))
    c = sorted(list(map(int, input().split())))

    # bを固定して、aとcを二分探索
    ans = 0

    for bi in b:
        i, _ = bisect_lt(a, bi)
        j, _ = bisect_gt(c, bi)

        if i is None or j is None:
            continue

        ans += (i + 1) * (n - j)

    print(ans)


if __name__ == "__main__":
    main()
