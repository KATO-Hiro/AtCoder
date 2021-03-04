# -*- coding: utf-8 -*-


class BIT:
    """Binary Indexed Tree (Fenwick Tree)
    Args:
        size: List size (greater than 0).
    """

    def __init__(self, size: int):
        self.size = size
        self._bit = [0 for _ in range(self.size + 1)]

    def add(self, index: int, value: int) -> None:
        """Adds value to list with index i.
        Args:
            index: The number of index (1-indexed).
            value: A value
        Landau notation: O(log n)
        """

        while index <= self.size:
            self._bit[index] += value
            index += index & -index

    def sum(self, index) -> int:
        """Calculate the sum of elements from 1 to index.
        Args:
            index: The number of index (1-indexed).
        Returns:
            The sum of elements from 1 to index.
        Landau notation: O(log n)
        """

        summed = 0

        while index > 0:
            summed += self._bit[index]
            index -= index & -index

        return summed


def main():
    from math import ceil
    from bisect import bisect_right
    import sys

    input = sys.stdin.readline

    n, d, a = map(int, input().split())
    p = sorted([list(map(int, input().split())) for _ in range(n)])
    xs = [xi for xi, _ in p]

    bit = BIT(n + 1)
    ans = 0

    for index, (xi, hi) in enumerate(p, 1):
        hi -= bit.sum(index)

        if hi <= 0:
            continue

        bomb_count = ceil(hi / a)
        ans += bomb_count
        damage = a * bomb_count
        bit.add(index, damage)
        # pos = bisect_right(xs, min(xi + 2 * d, 10 ** 9 + 7))
        pos = bisect_right(xs, xi + 2 * d)
        bit.add(pos + 1, -damage)

    print(ans)


if __name__ == "__main__":
    main()
