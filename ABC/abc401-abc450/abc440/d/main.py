# -*- coding: utf-8 -*-


from bisect import bisect_right
from typing import Tuple, List


def bisect_le(sorted_array: List[int], value: int) -> Tuple[int, int]:
    """Find the largest element <= value and its index, or (-1, 0) if it doesn't exist."""

    if sorted_array and sorted_array[0] <= value:
        index: int = bisect_right(sorted_array, value) - 1

        return index, sorted_array[index]

    return -1, 0


def main():
    n, q = list(map(int, input().split()))
    inf = 10**18
    a = [-inf] + sorted(list(map(int, input().split()))) + [inf]

    def f(zj, a):
        i, _ = bisect_le(a, zj)  # the largest element <= zj
        count = 0

        if i != -1:
            count = i + 1

        return zj - count

    def solve():
        xj, yj = list(map(int, input().split()))
        ng, ok = xj - 1, xj + yj + n + 1

        while abs(ok - ng) > 1:
            wj = (ok + ng) // 2

            if f(wj, a) - f(xj - 1, a) >= yj:
                ok = wj
            else:
                ng = wj

        print(ok)

    for _ in range(q):
        solve()


if __name__ == "__main__":
    main()
