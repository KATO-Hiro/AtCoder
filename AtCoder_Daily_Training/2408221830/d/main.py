# -*- coding: utf-8 -*-


def main():
    import sys

    sys.setrecursionlimit(10**8)

    input = sys.stdin.readline

    n, m = map(int, input().split())

    def dfs(array):
        if len(array) >= 2:
            if array[-2] >= array[-1]:
                return

        if len(array) == n:
            print(*array)

            return

        for i in range(1, m + 1):
            array.append(i)
            dfs(array)
            array.pop()

    dfs([])


if __name__ == "__main__":
    main()
