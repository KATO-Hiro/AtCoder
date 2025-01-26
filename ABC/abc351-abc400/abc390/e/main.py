# -*- coding: utf-8 -*-

from bisect import bisect_left
from typing import List


def bisect_ge(sorted_array: List[int], value: int):
    """Find the smallest element >= x and its index, or None if it doesn't exist."""

    if sorted_array[-1] >= value:
        index: int = bisect_left(sorted_array, value)

        return index, sorted_array[index]

    return None, None


def main():
    import sys

    input = sys.stdin.readline

    n, x = map(int, input().split())
    foods = [list() for _ in range(3)]

    for _ in range(n):
        vi, ai, ci = map(int, input().split())
        vi -= 1
        foods[vi].append((ai, ci))

    vitamins = list()

    # 各ビタミンについて、ナップサック問題
    for food in foods:
        dp = [0 for _ in range(x + 1)]

        for fi in food:
            ndp = [0 for _ in range(x + 1)]
            aj, cj = fi

            for j in range(x + 1):
                ndp[j] = max(ndp[j], dp[j])
                nj = j + cj

                if nj > x:
                    continue

                ndp[nj] = max(ndp[nj], dp[j] + aj)

            dp = ndp

        vitamins.append(dp)

    # 最小値の最大化 = 二分探索
    ac, wa = 0, 10**9

    def f(wj):
        total = 0

        for i in range(3):
            if vitamins[i][x] < wj:
                return False

            j, _ = bisect_ge(vitamins[i], wj)

            if j is None:
                return False

            total += j

        return total <= x

    while abs(wa - ac) > 1:
        wj = (ac + wa) // 2

        if f(wj):
            ac = wj
        else:
            wa = wj

    print(ac)


if __name__ == "__main__":
    main()
