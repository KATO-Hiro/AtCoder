# -*- coding: utf-8 -*-


from typing import List


def get_kth_greatest_value(array: List[int], k: int) -> List[int]:
    """Get the K-th greatest value among the first i terms of array.
    For each i = K, K + 1, ..., N, find the above.
    Args:
        arrary: List of numbers.
        k     : The number of terms to be compared.
    Returns:
        ans: The K-th greatest values.
    Landau notation: O(nlog(n))
    See:
    https://atcoder.jp/contests/abc234/tasks/abc234_d
    https://atcoder.jp/contests/abc234/submissions/28385666
    """

    from heapq import heapify, heappushpop

    q = array[:k]
    heapify(q)
    ans = [q[0]]

    for vi in array[k:]:
        heappushpop(q, vi)
        ans.append(q[0])

    return ans


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    p = list(map(int, input().split()))

    results = get_kth_greatest_value(p, k)
    print(*results, sep="\n")


if __name__ == "__main__":
    main()
