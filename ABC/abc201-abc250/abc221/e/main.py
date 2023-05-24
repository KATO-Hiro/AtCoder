# -*- coding: utf-8 -*-

import typing


class FenwickTree:
    """Reference: https://en.wikipedia.org/wiki/Fenwick_tree"""

    def __init__(self, n: int = 0, mod=None) -> None:
        self._n = n
        self.data = [0] * n
        self.mod = mod

    def add(self, p: int, x: typing.Any) -> None:
        assert 0 <= p < self._n

        p += 1

        while p <= self._n:
            self.data[p - 1] += x

            if self.mod is not None:
                self.data[p - 1] %= self.mod

            p += p & -p

    def sum(self, left: int, right: int) -> typing.Any:
        """[left, right)"""
        assert 0 <= left <= right <= self._n

        return self._sum(right) - self._sum(left)

    def _sum(self, r: int) -> typing.Any:
        s = 0

        while r > 0:
            s += self.data[r - 1]

            if self.mod is not None:
                s %= self.mod

            r -= r & -r

        return s


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


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))

    # Aiの左右の端部l, rを固定すると[l + 1, r)は自由に決められるので、2 ** (r - l - 1)通り

    # O(n ** 2)の高速化:
    # ・変数を分離すると、2 ** (r - 1) * ((1 / 2) ** l)
    # ・rを固定して、a[l] <= a[r]となる((1 / 2) ** l)を答えに加算
    # ・点加算と区間和を高速に求められるFenwick Treeを使用
    # ・各Aiに対して、((1 / 2) ** l)を加算
    # ・Aiが大きくなる可能性がある + 値そのもの以上に大小関係が重要なので、座標圧縮
    c = compress_coordinate(a)
    size = len(c.keys())
    mod = 998244353
    ft = FenwickTree(size + 1, mod)
    inv = pow(2, mod - 2, mod)  # 1 / p
    two, inv_two = 1, 1
    ans = 0

    for ai in a:
        d = c[ai]
        ans += two * ft.sum(0, d + 1)  # [l, r)
        ans %= mod

        two *= 2
        two %= mod
        inv_two *= inv
        inv_two %= mod

        ft.add(d, inv_two)

    print(ans)


if __name__ == "__main__":
    main()
