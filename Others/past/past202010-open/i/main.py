# -*- coding: utf-8 -*-

from bisect import bisect_right
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
    a = list(map(int, input().split()))
    b = a + a
    acc = list(accumulate(b, initial=0))
    total = sum(a)
    half = total // 2
    ans = 10**18

    for i in range(1, n + 1):
        _, value = bisect_le(acc, acc[i] + half)  # the largest element <= x

        if value is None:
            continue

        x = value - acc[i - 1]
        y = total - x
        ans = min(ans, abs(x - y))

    print(ans)


if __name__ == "__main__":
    main()
