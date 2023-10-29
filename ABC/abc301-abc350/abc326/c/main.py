# -*- coding: utf-8 -*-


from bisect import bisect_left, bisect_right
from typing import List


def bisect_lt(sorted_array: List[int], value: int):
    """Find the largest element < x and its index, or None if it doesn't exist."""

    if sorted_array[0] < value:
        index: int = bisect_left(sorted_array, value) - 1

        return index, sorted_array[index]

    return None, None


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    ans = 1

    for i, ai in enumerate(a):
        j, value = bisect_lt(a, ai + m)  # the largest element < x

        if j is not None:
            count = j - i + 1
            ans = max(ans, count)

    print(ans)


if __name__ == "__main__":
    main()
