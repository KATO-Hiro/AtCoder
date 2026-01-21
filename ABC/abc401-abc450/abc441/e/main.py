# -*- coding: utf-8 -*-

from typing import Any


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
            index += index & -index

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

        return summed


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = input().rstrip()
    d = [n]

    for si in s:
        d.append(d[-1])

        if si == "A":
            d[-1] += 1
        elif si == "B":
            d[-1] -= 1

    size = 2 * n + 1
    bit = BIT(size)
    ans = 0

    for di in d:
        ans += bit.range_sum(0, di)
        bit.add(di, 1)

    print(ans)


if __name__ == "__main__":
    main()
