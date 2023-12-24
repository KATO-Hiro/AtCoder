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

    n, q = map(int, input().split())
    inf = 10**18
    r = sorted(list(map(int, input().split()))) + [inf]
    summed_r = list(accumulate(r, initial=0))
    # print(summed_r)

    for _ in range(q):
        qi = int(input())

        i, value = bisect_le(summed_r, qi)  # the largest element <= x

        if i is None:
            i = 0

        print(i)


if __name__ == "__main__":
    main()
