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

    n, t = map(int, input().split())
    s = input().rstrip()
    x = list(map(int, input().split()))

    # 正の方向を向いている蟻iを固定したときに、負の方向を向いている蟻jの数(蟻iの位置xi + 2 * t以下)の合計
    # 蟻の位置を昇順ソート + 単調性から二分探索
    y = list()

    for xi, si in zip(x, s):
        if si == "1":
            continue

        y.append(xi)

    inf = 10**18
    y = [-inf] + sorted(y) + [inf]
    ans = 0

    for xi, si in zip(x, s):
        if si == "0":
            continue

        j, _ = bisect_le(y, xi + 2 * t)
        i, _ = bisect_le(y, xi)

        if i is None or j is None:
            continue

        ans += max(j - i, 0)

    print(ans)


if __name__ == "__main__":
    main()
