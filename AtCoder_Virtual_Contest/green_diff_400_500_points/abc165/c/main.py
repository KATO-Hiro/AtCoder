# -*- coding: utf-8 -*-

ans = 0


def main():
    import sys

    sys.setrecursionlimit(10**8)

    input = sys.stdin.readline

    n, m, q = map(int, input().split())
    abcd = [tuple(map(int, input().split())) for _ in range(q)]

    def dfs(i, array):
        global ans

        if i == n:
            summed = 0

            for ai, bi, ci, di in abcd:
                ai -= 1
                bi -= 1

                if array[bi] - array[ai] == ci:
                    summed += di

            ans = max(ans, summed)

            return

        for j in range(1, m + 1):
            if len(array) >= 1 and array[-1] > j:
                continue

            array.append(j)
            dfs(i + 1, array)
            array.pop()

    dfs(0, [])
    print(ans)


if __name__ == "__main__":
    main()
