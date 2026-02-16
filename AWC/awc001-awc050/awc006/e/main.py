# -*- coding: utf-8 -*-

from typing import Any, List


class BIT:
    """Binary Indexed Tree (Fenwick Tree)

    See:
    https://atcoder.jp/contests/tessoku-book/submissions/34912434
    """

    def __init__(self, size: int) -> None:
        self.size = size
        self.size0 = 1 << (size.bit_length() - 1)
        self.tree = [0] * (size + 1)

    def add(self, index: int, value: Any) -> None:
        assert 0 <= index < self.size

        index += 1

        while index <= self.size:
            self.tree[index] += value
            # self.tree[index] %= mod
            index += index & -index

    def get(self, index: int) -> Any:
        return self.sum(index) - self.sum(index - 1)

    def range_sum(self, left: int, right: int) -> Any:
        assert 0 <= left <= right <= self.size

        return self.sum(right - 1) - self.sum(left - 1)

    def sum(self, index: int) -> Any:
        index += 1
        summed = 0

        assert 0 <= index <= self.size

        while index > 0:
            summed += self.tree[index]
            index -= index & -index
            # summed %= mod

        return summed


def main():
    import sys

    input = sys.stdin.readline

    n, q = map(int, input().split())
    s = list(map(int, input().split()))
    bit = BIT(n + 10)

    for i, si in enumerate(s):
        bit.add(i, si)

    for _ in range(q):
        query = list(map(int, input().split()))

        if query[0] == 1:
            l, r = query[1:]
            l -= 1

            ans = bit.range_sum(l, r)
            print(ans)
        else:
            x, v = query[1:]
            x -= 1
            value = bit.get(x)
            bit.add(x, -value + v)


if __name__ == "__main__":
    main()
