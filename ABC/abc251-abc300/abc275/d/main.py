# -*- coding: utf-8 -*-


from functools import lru_cache


@lru_cache(maxsize=10 ** 6)
def dfs(i):
    if i == 0:
        return 1

    return dfs((i // 2)) + dfs(i // 3)


def main():
    import sys
    sys.setrecursionlimit(10 ** 7)

    input = sys.stdin.readline

    n = int(input())
    print(dfs(n))


if __name__ == "__main__":
    main()

