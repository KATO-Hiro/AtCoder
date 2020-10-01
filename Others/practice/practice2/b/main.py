# -*- coding: utf-8 -*-


# See:
# https://github.com/not522/ac-library-python/blob/master/atcoder/fenwicktree.py
import typing


class FenwickTree:
    '''Reference: https://en.wikipedia.org/wiki/Fenwick_tree'''

    def __init__(self, n: int = 0) -> None:
        self._n = n
        self.data = [0] * n

    def add(self, p: int, x: typing.Any) -> None:
        assert 0 <= p < self._n

        p += 1
        while p <= self._n:
            self.data[p - 1] += x
            p += p & -p

    def sum(self, left: int, right: int) -> typing.Any:
        assert 0 <= left <= right <= self._n

        return self._sum(right) - self._sum(left)

    def _sum(self, r: int) -> typing.Any:
        s = 0
        while r > 0:
            s += self.data[r - 1]
            r -= r & -r

        return s


def main():
    import sys
    input = sys.stdin.readline

    n, q = map(int, input().split())
    a = list(map(int, input().split()))

    fenwicktree = FenwickTree(n)

    for index, ai in enumerate(a):
        fenwicktree.add(p=index, x=ai)

    for _ in range(q):
        number, first, second = input().split()

        if number == '0':
            fenwicktree.add(p=int(first), x=int(second))
        else:
            print(fenwicktree.sum(left=int(first), right=int(second)))


if __name__ == '__main__':
    main()
