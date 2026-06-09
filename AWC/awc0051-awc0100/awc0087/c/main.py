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
    from itertools import accumulate, pairwise

    input = sys.stdin.readline

    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = [abs(ai - aj) for ai, aj in pairwise(a)]
    inf = 10**20
    acc = list(accumulate(b, initial=0)) + [inf]
    ans = inf

    for i in range(n):
        j, _ = bisect_ge(acc, acc[i] + k)

        if i > j or j == n:
            continue

        ans = min(ans, j - i + 1)

    if ans == inf:
        ans = -1

    print(ans)


if __name__ == "__main__":
    main()
