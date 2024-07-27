# -*- coding: utf-8 -*-

from typing import Any


def compress_coordinate(elements: list) -> dict:
    """Means that reduce the numerical value while maintaining the magnitude
        relationship.

    Args:
        elements: list of integer numbers (greater than -1).

    Returns:
        A dictionary's items ((original number, compressed number) pairs).

    Landau notation: O(n log n)
    """

    # See:
    # https://atcoder.jp/contests/abc036/submissions/5707999?lang=ja
    compressed_list = sorted(set(elements))
    return {element: index for index, element in enumerate(compressed_list)}


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

    def lower_bound(self, value: Any) -> int:
        pos = 0
        plus = self.size0

        while plus > 0:
            if pos + plus <= self.size and self.tree[pos + plus] < value:
                value -= self.tree[pos + plus]
                pos += plus

            plus //= 2

        return pos


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    c = compress_coordinate(a)
    count = BIT(n)
    summed = BIT(n)
    ans = 0

    for ai in a:
        ci = c[ai]

        ans += count.range_sum(0, ci) * ai
        ans -= summed.range_sum(0, ci)

        count.add(ci, 1)
        summed.add(ci, ai)

    print(ans)


if __name__ == "__main__":
    main()
