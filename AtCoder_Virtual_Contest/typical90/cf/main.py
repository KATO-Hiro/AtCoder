# -*- coding: utf-8 -*-

from bisect import bisect_left, bisect_right
from typing import List


def bisect_gt(sorted_array: List[int], value: int):
    """Find the smallest element > x and its index, or None if it doesn't exist."""

    if sorted_array[-1] > value:
        index: int = bisect_right(sorted_array, value)

        return index, sorted_array[index]

    return None, None


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = input().rstrip()
    maru = [0] * n
    batsu = [0] * n

    for i, si in enumerate(s):
        if i > 0:
            maru[i] = maru[i - 1]
            batsu[i] = batsu[i - 1]

        if si == "o":
            maru[i] += 1
        else:
            batsu[i] += 1

    ans = 0

    for left, si in enumerate(s):
        if si == "o":
            count = batsu[left]
            j, value = bisect_gt(batsu, count)  # the smallest element > x
        else:
            count = maru[left]
            j, value = bisect_gt(maru, count)  # the smallest element > x

        if j is not None:
            ans += n - j

    print(ans)


if __name__ == "__main__":
    main()
