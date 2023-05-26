# -*- coding: utf-8 -*-

from bisect import bisect_left, bisect_right
from typing import List


def bisect_ge(sorted_array: List[int], value: int):
    """Find the smallest element >= x and its index, or None if it doesn't exist."""

    if sorted_array[-1] >= value:
        index: int = bisect_left(sorted_array, value)

        return index, sorted_array[index]

    return None, None


def main():
    import sys

    input = sys.stdin.readline

    n, q = map(int, input().split())
    a = sorted(list(map(int, input().split())))

    for _ in range(q):
        xi = int(input())
        index, value = bisect_ge(a, xi)

        if index is None:
            print(0)
        else:
            print(n - index)


if __name__ == "__main__":
    main()
