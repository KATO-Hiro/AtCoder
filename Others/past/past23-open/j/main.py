# -*- coding: utf-8 -*-

from bisect import bisect_left, bisect_right


def bisect_lt(sorted_array: list[int], value: int):
    """Find the largest element < x and its index, or None if it doesn't exist."""

    if sorted_array[0] < value:
        index: int = bisect_left(sorted_array, value) - 1

        return index, sorted_array[index]

    return None, None


def bisect_gt(sorted_array: list[int], value: int):
    """Find the smallest element > x and its index, or None if it doesn't exist."""

    if sorted_array[-1] > value:
        index: int = bisect_right(sorted_array, value)

        return index, sorted_array[index]

    return None, None


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s, t = [], []
    intervals = []

    for _ in range(n):
        si, ti = map(int, input().split())

        s.append(si)
        t.append(ti)
        intervals.append((si, ti))

    s.sort()
    t.sort()
    ans = []

    for si, ti in intervals:
        i, _ = bisect_lt(t, si)  # the largest element < si
        j, value = bisect_gt(s, ti)  # the smallest element > ti

        count = 0

        if i is not None:
            count += i + 1
        if j is not None:
            count += n - j

        ans.append(n - 1 - count)

    print(*ans)


if __name__ == "__main__":
    main()
