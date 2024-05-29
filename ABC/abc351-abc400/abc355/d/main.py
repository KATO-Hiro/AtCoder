# -*- coding: utf-8 -*-


class SegmentTree:
    def __init__(self, size):
        self.size = 2 ** ((size - 1).bit_length())
        self.tree = [0] * (2 * self.size)

    def add(self, i, x):
        i += self.size
        self.tree[i] += x

        while i > 1:
            self.tree[i >> 1] = self.tree[i] + self.tree[i ^ 1]
            i >>= 1

    def query(self, l, r):
        l += self.size
        r += self.size
        s = 0

        while l < r:
            if l & 1:
                s += self.tree[l]
                l += 1
            if r & 1:
                r -= 1
                s += self.tree[r]

            l >>= 1
            r >>= 1

        return s


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

    n = int(input())
    lr = [tuple(map(int, input().split())) for _ in range(n)]
    lr = sorted(lr)
    l = [li for li, _ in lr]
    # 座標圧縮
    compressed = {x: i for i, x in enumerate(sorted(set(l)))}
    st = SegmentTree(len(compressed))

    for i in range(n):
        li, _ = lr[i]
        st.add(compressed[li], 1)

    ans = 0

    for j in range(n - 1):
        lj, rj = lr[j]
        st.add(compressed[lj], -1)

        # li <= rjとなる個数
        _, value = bisect_le(l, rj)

        if value is None:
            continue

        count = st.query(0, compressed[value] + 1)
        ans += count

    print(ans)


if __name__ == "__main__":
    main()
