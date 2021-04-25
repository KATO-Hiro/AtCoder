# -*- coding: utf-8 -*-

from typing import Tuple


def extgcd(a: int, b: int) -> Tuple[int, int, int]:
    """a * x + b * y = gcd(a, b)

    See:
    https://qiita.com/drken/items/b97ff231e43bce50199a
    https://www.youtube.com/watch?v=hY2FicqnAcc

    O(gcd(a, b))
    """

    if b == 0:
        return (a, 1, 0)

    g, x, y = extgcd(b, a % b)

    return g, y, x - (a // b) * y


def main():
    import sys

    input = sys.stdin.readline
    sys.setrecursionlimit(10 ** 7)

    t = int(input())

    for i in range(t):
        n, s, k = map(int, input().split())
        g, x, y = extgcd(k, n)

        if s % g != 0:
            print(-1)
        else:
            n, s, k = n // g, s // g, k // g

            print((((-s * x) % n) + n) % n)


if __name__ == "__main__":
    main()
