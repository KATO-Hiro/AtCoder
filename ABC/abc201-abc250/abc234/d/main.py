# -*- coding: utf-8 -*-


from typing import List


def get_kth_greatest_value(array: List[int], k: int) -> List[int]:
    """
    See:
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

    for result in results:
        print(result)
    

if __name__ == "__main__":
    main()
