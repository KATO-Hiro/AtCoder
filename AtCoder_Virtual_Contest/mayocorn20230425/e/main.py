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


def count(x):
    size = len(x)
    bit = BIT(size)
    ans = 0
    
    for i, xi in enumerate(x):
        ans += i - bit.sum(xi)
        bit.add(xi, 1)

    return ans


def compress_coordinate(elements: list) -> dict:
    ''' Means that reduce the numerical value while maintaining the magnitude
        relationship.
    Args:
        elements: list of integer numbers (greater than -1).
    Returns:
        A dictionary's items ((original number, compressed number) pairs).
    Landau notation: O(n log n)
    '''

    # See:
    # https://atcoder.jp/contests/abc036/submissions/5707999?lang=ja
    compressed_list = sorted(set(elements))
    return {element: index for index, element in enumerate(compressed_list)}


def main():
    from collections import defaultdict
    import sys

    input = sys.stdin.readline

    n = int(input())
    c = list(map(int, input().split()))
    x = list(map(int, input().split()))

    # 転倒数
    # 色を識別しない場合 - 同じ色の場合
    ans = count(x)

    # 同じ色の場合
    # 数字をまとめる + 座標圧縮
    d = defaultdict(list)

    for ci, xi in zip(c, x):
        if ci not in d.keys():
            d[ci] = [xi]
        else:
            d[ci].append(xi)

    for values in d.values():
        compressed_values = compress_coordinate(values)
        e = [compressed_values[value] + 1 for value in values]

        ans -= count(e)

    print(ans)


if __name__ == "__main__":
    main()
