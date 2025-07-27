# -*- coding: utf-8 -*-


def main():
    import sys

    sys.setrecursionlimit(10**7)

    input = sys.stdin.readline

    n, k, x = map(int, input().split())
    s = [input().rstrip() for _ in range(n)]
    candidates = list()

    def dfs(array):
        nonlocal candidates

        if len(array) == k:
            candidates.append("".join(array))
            return

        for i in range(n):
            array.append(s[i])
            dfs(array)
            array.pop()

    dfs([])
    candidates.sort()
    print(candidates[x - 1])


if __name__ == "__main__":
    main()
