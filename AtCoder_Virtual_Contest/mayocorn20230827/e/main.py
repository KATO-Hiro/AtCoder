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
    from itertools import product

    input = sys.stdin.readline

    n, t = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    m = n // 2
    inf = 10**18
    b, c = a[:m], a[m:]
    summed_b = set()
    summed_c = list()

    for pattern in product([0, 1], repeat=m):
        summed = 0

        for pi, bi in zip(pattern, b):
            if pi == 1:
                summed += bi

        summed_b.add(summed)

    for pattern in product([0, 1], repeat=n - m):
        summed = 0

        for pi, ci in zip(pattern, c):
            if pi == 1:
                summed += ci

        summed_c.append(summed)

    ans = 0
    summed_c = sorted(summed_c)

    for sb in summed_b:
        diff = t - sb

        if diff < 0:
            continue

        i, value = bisect_le(summed_c, diff)

        if value == inf:
            continue

        candidate = sb + value

        if candidate <= t:
            ans = max(ans, candidate)

    print(ans)


if __name__ == "__main__":
    main()
