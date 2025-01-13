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

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    ans = 0

    for ai in a:
        i, _ = bisect_le(a, ai // 2)  # the largest element <= x

        if i is  None:
            continue

        ans += i + 1

    print(ans)



if __name__ == "__main__":
    main()
