# -*- coding: utf-8 -*-


def main():
    import sys

    from functools import lru_cache

    sys.setrecursionlimit(10**8)

    input = sys.stdin.readline

    x = int(input())
    mod = 998244353

    @lru_cache(None)
    def f(n):
        if n <= 4:
            return n

        f1 = f(n // 2)
        f2 = f((n + 1) // 2)

        return (f1 * f2) % mod

    ans = f(x)
    print(ans)


if __name__ == "__main__":
    main()
