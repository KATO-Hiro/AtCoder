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

    n, m = map(int, input().split())
    x, c = [0], [0]

    for _ in range(n):
        xi, ci = map(int, input().split())
        x.append(xi)
        c.append(ci)

    acc = list(accumulate(c))
    ans = 0

    for left in range(1, n + 1):
        right, _ = bisect_le(acc, acc[left - 1] + m)
        ans = max(ans, x[right] - x[left])

    print(ans)


if __name__ == "__main__":
    main()
