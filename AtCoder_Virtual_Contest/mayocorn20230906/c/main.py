# -*- coding: utf-8 -*-

from functools import lru_cache


def main():
    import sys

    sys.setrecursionlimit(10**8)

    input = sys.stdin.readline

    n = int(input())

    @lru_cache(maxsize=None)
    def rec(k):
        if k == 0:
            return 1

        ans = 0
        ans += rec(k // 2) + rec(k // 3)

        return ans

    print(rec(n))


if __name__ == "__main__":
    main()
