# -*- coding: utf-8 -*-


def main():
    from functools import lru_cache

    import sys
    sys.setrecursionlimit(10 ** 8)

    input = sys.stdin.readline

    n = int(input())
    mod = 998244353
    inv = pow(5, mod - 2, mod)  # 1 / p


    # メモ化再帰
    @lru_cache(maxsize=None)
    def f(i):
        if i == 1:
            return 1
        
        results = 0

        for j in range(2, 6 + 1):
            if i % j != 0:
                continue

            results += f(i // j)
            results %= mod
        
        results *= inv
        results %= mod

        return results

    print(f(n))


if __name__ == "__main__":
    main()
