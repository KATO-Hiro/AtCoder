# -*- coding: utf-8 -*-


from bisect import bisect_left, bisect_right
from typing import List


def bisect_lt(sorted_array: List[int], value: int):
    """Find the largest element < x and its index, or None if it doesn't exist."""

    if sorted_array[0] < value:
        index: int = bisect_left(sorted_array, value) - 1

        return index, sorted_array[index]

    return None, None


def main():
    import sys
    from collections import defaultdict

    input = sys.stdin.readline

    w, h = map(int, input().split())
    n = int(input())
    pq = [tuple(map(int, input().split())) for _ in range(n)]
    a_count = int(input())
    a = [0] + list(map(int, input().split())) + [w]
    b_count = int(input())
    b = [0] + list(map(int, input().split())) + [h]
    ans = defaultdict(int)

    for pi, qi in pq:
        i, value1 = bisect_lt(a, pi)
        j, value2 = bisect_lt(b, qi)
        ans[(i, j)] += 1

    if (a_count + 1) * (b_count + 1) - len(ans.keys()) > 0:
        print(0, max(ans.values()))
    else:
        print(min(ans.values()), max(ans.values()))


if __name__ == "__main__":
    main()
