# -*- coding: utf-8 -*-


def main():
    import sys

    from functools import lru_cache

    sys.setrecursionlimit(10**8)

    input = sys.stdin.readline
    x, y = map(int, input().split())

    @lru_cache(None)
    def f(n):
        if n <= 0:
            return 0
        elif n == 1:
            return x
        elif n == 2:
            return y

        value = f(n - 1) + f(n - 2)
        value = list(str(value))[::-1]

        return int("".join(value))

    print(f(10))


if __name__ == "__main__":
    main()
