# -*- coding: utf-8 -*-

from typing import List


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


# See:
# https://ikatakos.com/pot/programming_algorithm/dynamic_programming/inversion
def calc_inversion_number(array: List[int]) -> int:
    compressed_dict = {
        element: index for index, element in enumerate(sorted(set(array)), 1)
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

    n = int(input())
    a = list(map(int, input().split()))
    result = calc_inversion_number(a)
    print(result)


if __name__ == "__main__":
    main()
