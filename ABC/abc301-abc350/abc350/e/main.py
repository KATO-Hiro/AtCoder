# -*- coding: utf-8 -*-


def main():
    import functools
    import sys

    sys.setrecursionlimit(10**8)

    input = sys.stdin.readline

    n, a, x, y = map(int, input().split())

    @functools.lru_cache(maxsize=None)
    def f(m):
        if m == 0:
            return 0

        expected = x + f(m // a)
        dice = y

        for b in range(2, 6 + 1):
            dice += y + f(m // b)

        return min(expected, dice / 5)

    print(f(n))


if __name__ == "__main__":
    main()
