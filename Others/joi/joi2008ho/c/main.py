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

    n, m = map(int, input().split())
    p = [int(input()) for _ in range(n)] + [0]
    pair_scores = []

    for pi in p:
        for pj in p:
            sub_total = pi + pj

            if sub_total > m:
                continue

            pair_scores.append(sub_total)

    pair_scores.sort()
    ans = 0

    for ps in pair_scores:
        remain = m - ps
        _, value = bisect_le(pair_scores, remain)

        if value is None:
            continue
        if ps + value > m:
            continue

        ans = max(ans, ps + value)

    print(ans)


if __name__ == "__main__":
    main()
