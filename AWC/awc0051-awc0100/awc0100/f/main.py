# -*- coding: utf-8 -*-

from bisect import bisect_left
from typing import List


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

    n, k = map(int, input().split())
    v = list(map(int, input().split()))
    acc = list(accumulate(v, initial=0))
    ans = 0

    for i in range(0, n + 1):
        j, _ = bisect_ge(acc, acc[i] + k)

        if j is None:
            continue

        ans += n - j + 1

    print(ans)


if __name__ == "__main__":
    main()
