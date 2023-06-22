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

    n, w, l, r = map(int, input().split())
    x = [0] + list(map(int, input().split())) + [w]

    # 貰うdp + 連続した区間の和 = 累積和
    dp, summed = [0] * (n + 2), [0] * (n + 2)
    dp[0] = summed[0] = 1
    mod = 10**9 + 7

    for i in range(1, n + 2):
        xi = x[i]
        # [xi - r, xi - l]となる区間を二分探索で求める

        pos_left, _ = bisect_ge(x, xi - r)
        pos_right, _ = bisect_le(x, xi - l)

        # 累積和で高速化
        if pos_right is not None:
            dp[i] = summed[pos_right]

            if pos_left - 1 >= 0:
                dp[i] -= summed[pos_left - 1]

            dp[i] %= mod

        summed[i] = summed[i - 1] + dp[i]
        summed[i] %= mod

    print(dp[n + 1])


if __name__ == "__main__":
    main()
