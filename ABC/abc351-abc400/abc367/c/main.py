# -*- coding: utf-8 -*-


import sys

sys.setrecursionlimit(10**8)

input = sys.stdin.readline

n, k = map(int, input().split())
r = list(map(int, input().split()))


def dfs(a, i):
    if len(a) == n and sum(a) % k == 0:
        print(*a)
        return

    if i >= n:
        return

    for value in range(1, r[i] + 1):
        a.append(value)
        dfs(a, i + 1)
        a.pop()


dfs([], 0)
