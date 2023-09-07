# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict

    sys.setrecursionlimit(10**8)

    input = sys.stdin.readline

    s = int(input())
    memo = defaultdict(list)

    def dfs(i, n):
        if n in memo.keys():
            print(i)
            return

        memo[n] = i

        if n % 2 == 0:
            dfs(i + 1, n // 2)
        else:
            dfs(i + 1, 3 * n + 1)

    dfs(1, s)


if __name__ == "__main__":
    main()
