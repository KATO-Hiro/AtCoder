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

    input = sys.stdin.readline

    n, t = input().rstrip().split()
    n = int(n)
    m = len(t)
    t_rev = t[::-1]
    left, right = list(), list()

    # Siの前と後ろから、tとどこまで一致するかGreedyに求める
    for _ in range(n):
        si = input().rstrip()

        i = 0

        for sij in si:
            while i < m and sij == t[i]:
                i += 1
                break

        left.append(i)

        j = 0

        for sij in si[::-1]:
            while j < m and sij == t_rev[j]:
                j += 1
                break

        right.append(j)

    # print(left)
    # print(right)

    # 左側の一致する個数Li + 右側の一致する個数Rjが|T|以上なら条件を満たす
    # LとRを独立に考えて、上記の条件を満たす場合を数える
    # Lを全探索、Rを二分探索
    right.sort()
    ans = 0

    for li in left:
        j, value = bisect_ge(right, m - li)  # the smallest element >= x

        if j is not None:
            count = n - j
            ans += count
            # print(j, count)

    print(ans)


if __name__ == "__main__":
    main()
