# -*- coding: utf-8 -*-


import re


def main():
    import sys

    sys.setrecursionlimit(10**8)

    input = sys.stdin.readline

    n, m = map(int, input().split())
    c = list(map(int, input().split()))
    b = [[] for _ in range(n)]

    for i in range(m):
        ki, *ai = map(int, input().split())

        for aij in ai:
            aij -= 1
            b[aij].append(i)

    inf = 10**18
    ans = inf

    def dfs(i, a):
        nonlocal ans

        if i == n:
            freq = [0] * m

            for ai, bi in zip(a, b):
                for bij in bi:
                    freq[bij] += ai

            ok = all(f >= 2 for f in freq)

            if ok:
                candidate = 0

                for ai, ci in zip(a, c):
                    candidate += ai * ci

                ans = min(ans, candidate)

            return

        for j in range(3):
            a.append(j)
            dfs(i + 1, a)
            a.pop()

    dfs(0, [])
    print(ans)


if __name__ == "__main__":
    main()
