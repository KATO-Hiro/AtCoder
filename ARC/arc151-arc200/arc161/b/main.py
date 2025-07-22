# -*- coding: utf-8 -*-

from bisect import bisect_right
from typing import List


def bisect_le(sorted_array: List[int], value: int):
    """Find the largest element <= x and its index, or None if it doesn't exist."""

    if sorted_array[0] <= value:
        index: int = bisect_right(sorted_array, value) - 1

        return index, sorted_array[index]

    return None, None


def solve(candidates):
    n = int(input())

    _, value = bisect_le(candidates, n)

    if value is None:
        print(-1)
    else:
        print(value)


def main():
    import sys

    input = sys.stdin.readline

    t = int(input())

    from itertools import combinations

    candidates = []

    m = 60

    for i, j, k in combinations(range(m), 3):
        if i == j or j == k or i == k:
            continue

        candidate = 2**i + 2**j + 2**k
        candidates.append(candidate)

    candidates.sort()

    for _ in range(t):
        solve(candidates)


if __name__ == "__main__":
    main()
