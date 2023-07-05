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
    from itertools import accumulate

    input = sys.stdin.readline

    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(accumulate([0] + a))
    ans = 0

    for i in range(1, n + 1):
        j, value = bisect_ge(b, b[i - 1] + k)  # the smallest element >= x

        if j is not None:
            count = n - j + 1
            ans += count

    print(ans)


if __name__ == "__main__":
    main()
