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
            # self.tree[index] %= mod
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
            # summed %= mod

        return summed


def main():
    import sys
    from itertools import accumulate

    input = sys.stdin.readline

    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    s = [0]

    for ai in a:
        si = s[-1] + ai
        si %= m
        s += [si]

    acc_s = list(accumulate(s))
    bit = BIT(m)
    ans = 0

    # (s[right] - s[left - 1]) % modの括弧内が負の値になる場合があるため、+m する必要がある
    # その個数を高速に数えるには、1点更新と区間和が取れるBITを使う
    for right in range(1, n + 1):
        ans += s[right] * right - acc_s[right - 1] + m * bit.range_sum(s[right] + 1, m)
        bit.add(s[right], 1)

    print(ans)


if __name__ == "__main__":
    main()
