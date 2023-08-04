# -*- coding: utf-8 -*-


ans = 0


def main():
    import sys
    from functools import lru_cache

    input = sys.stdin.readline

    h = int(input())

    @lru_cache(maxsize=None)
    def rec(i):
        global ans

        if i == 1:
            return 1

        if i > 1:
            ans += rec(i // 2) + rec(i // 2)

        return ans

    print(2 * rec(h) - 1)


if __name__ == "__main__":
    main()
