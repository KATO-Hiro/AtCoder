# -*- coding: utf-8 -*-

from bisect import bisect_left, bisect_right
from typing import List


def bisect_lt(sorted_array: List[int], value: int):
    """Find the largest element < x and its index, or None if it doesn't exist."""

    if sorted_array[0] < value:
        index: int = bisect_left(sorted_array, value) - 1

        return index, sorted_array[index]

    return None, None


def main():
    import sys

    input = sys.stdin.readline

    n = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    q = int(input())

    for _ in range(q):
        xi = int(input())
        i, value = bisect_lt(a, xi)  # the largest element < x

        if i is not None:
            count = i + 1
        else:
            count = 0

        print(count)


if __name__ == "__main__":
    main()
