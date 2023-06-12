# -*- coding: utf-8 -*-

from bisect import bisect_left, bisect_right
from typing import List


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
    inf = 10**18
    c = [0] + list(accumulate(sorted(list(map(int, input().split()))))) + [inf]
    q = int(input())

    for _ in range(q):
        xi = int(input())
        i, value = bisect_le(c, xi)
        print(i)


if __name__ == "__main__":
    main()
