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
    from itertools import pairwise

    input = sys.stdin.readline

    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ids = []

    for bi in b:
        i, value = bisect_le(a, bi)  # the largest element <= bi
        count = 0

        if i is not None:
            count = i + 1

        ids.append(count)

    ans = 0

    for first, second in pairwise(ids):
        ans += abs(second - first)

    print(ans)


if __name__ == "__main__":
    main()
