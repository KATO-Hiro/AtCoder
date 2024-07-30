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

    input = sys.stdin.readline

    n, q = map(int, input().split())
    inf = 10**20
    a = [-inf] + sorted(list(map(int, input().split()))) + [inf]

    def f(wj, bj, kj):
        lower, upper = bj - wj, bj + wj

        i, _ = bisect_lt(a, lower)  # the largest element < x
        j, _ = bisect_le(a, upper)  # the largest element <= x

        return j - i >= kj

    for _ in range(q):
        bj, kj = map(int, input().split())

        ng, ok = -1, 2 * 10**8

        while abs(ok - ng) > 1:
            wj = (ok + ng) // 2

            if f(wj, bj, kj):
                ok = wj
            else:
                ng = wj

        print(ok)


if __name__ == "__main__":
    main()
