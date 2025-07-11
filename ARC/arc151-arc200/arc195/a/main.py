# -*- coding: utf-8 -*-

from bisect import bisect_right
from typing import List


def bisect_gt(sorted_array: List[int], value: int):
    """Find the smallest element > x and its index, or None if it doesn't exist."""

    if sorted_array[-1] > value:
        index: int = bisect_right(sorted_array, value)

        return index, sorted_array[index]

    return None, None


def main():
    import sys
    from collections import defaultdict

    input = sys.stdin.readline

    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans = list()

    for k in range(2):
        d = defaultdict(list)

        for i, ai in enumerate(a):
            d[ai].append(i)

        id = -1
        ok = True
        candidate = []

        for bj in b:
            f = d[bj]

            if len(f) == 0:
                ok = False
                break

            j, value = bisect_gt(f, id)

            if j is None or value is None:
                ok = False
                break

            if k == 0:
                candidate.append(value)
            else:
                candidate.append(n - 1 - value)

            id = value

        if ok:
            if k == 1:
                candidate = candidate[::-1]

            ans.append(candidate)

        a = a[::-1]
        b = b[::-1]

    if len(ans) == 2 and ans[0] != ans[1]:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
