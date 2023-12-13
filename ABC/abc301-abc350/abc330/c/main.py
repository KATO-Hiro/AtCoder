# -*- coding: utf-8 -*-


from bisect import bisect_left, bisect_right
from typing import List


def bisect_le(sorted_array: List[int], value: int):
    """Find the largest element <= x and its index, or None if it doesn't exist."""

    if sorted_array[0] <= value:
        index: int = bisect_right(sorted_array, value) - 1

        return index, sorted_array[index]

    return None, None


def bisect_ge(sorted_array: List[int], value: int):
    """Find the smallest element >= x and its index, or None if it doesn't exist."""

    if sorted_array[-1] >= value:
        index: int = bisect_left(sorted_array, value)

        return index, sorted_array[index]

    return None, None


def main():
    import sys

    input = sys.stdin.readline

    d = int(input())
    upper = 15 * 10**5
    ans = 10**18
    ys = [i**2 for i in range(upper + 1)]

    for x in range(upper + 1):
        diff = x**2 - d

        if diff < 0:
            diff_abs = abs(diff)

            _, y_min = bisect_le(ys, diff_abs)
            _, y_max = bisect_ge(ys, diff_abs)

            ans = min(ans, abs(diff + y_min), abs(diff + y_max))
        else:
            ans = min(ans, abs(diff))

    print(ans)


if __name__ == "__main__":
    main()
