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


# See:
# https://ikatakos.com/pot/programming_algorithm/dynamic_programming/inversion
def calc_inversion_number(array: list[int]) -> int:
    compressed_dict = {
        element: index for index, element in enumerate(sorted(set(array)))
    }
    compressed_list = [compressed_dict[ai] for ai in array]

    size = len(compressed_list)
    bit = BIT(size)
    inversion_number = 0

    for index, value in enumerate(compressed_list):
        inversion_number += index - bit.sum(value)
        bit.add(value, 1)

    return inversion_number


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    c = list()

    for i, ai in enumerate(a):
        c.append((ai, i))

    c.sort()
    count = calc_inversion_number(a)
    ans = list()

    for x in range(m - 1, -1, -1):
        ans.append(count)

        while c and c[-1][0] == x:
            _, j = c.pop()
            count += j
            count -= n - 1 - j

    print(*ans, sep="\n")


if __name__ == "__main__":
    main()
