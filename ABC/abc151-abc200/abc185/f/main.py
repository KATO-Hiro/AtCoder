# -*- coding: utf-8 -*-


import typing


class FenwickTree:
    """Reference: https://en.wikipedia.org/wiki/Fenwick_tree"""

    def __init__(self, n: int = 0) -> None:
        self._n = n
        self.data = [0] * n

    def add(self, p: int, x: typing.Any) -> None:
        assert 0 <= p < self._n

        p += 1
        while p <= self._n:
            self.data[p - 1] ^= x
            p += p & -p

    def sum(self, left: int, right: int) -> typing.Any:
        assert 0 <= left <= right <= self._n

        return self._sum(right) ^ self._sum(left)

    def _sum(self, r: int) -> typing.Any:
        s = 0
        while r > 0:
            s ^= self.data[r - 1]
            r -= r & -r

        return s


def main():
    import sys

    input = sys.stdin.readline

    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    bit = FenwickTree(n)

    for index, ai in enumerate(a):
        bit.add(index, ai)

    for i in range(q):
        ti, xi, yi = map(int, input().split())

        if ti == 1:
            bit.add(xi - 1, yi)
        else:
            summed = bit.sum(xi - 1, yi)
            print(summed)


if __name__ == "__main__":
    main()
