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
    a = list(map(int, input().split()))
    inf = 10**18
    d = [0] + sorted(a) + [inf]
    c = list(accumulate(d))
    ans = list()

    for ai in a:
        i, value = bisect_le(d, ai)  # the largest element <= x

        ans.append(c[n] - c[i])

    print(*ans)


if __name__ == "__main__":
    main()
