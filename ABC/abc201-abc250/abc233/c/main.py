# -*- coding: utf-8 -*-


import sys
sys.setrecursionlimit(10 ** 7)

input = sys.stdin.readline

n, x = map(int, input().split())
a = [[] for _ in range(n)]
size = [0 for _ in range(n)]

for i in range(n):
    l, *ai = map(int, input().split())
    size[i], a[i] = l, ai

def dfs(arr, j):
    if len(arr) == n:
        p = 1

        for ai in arr:
            p *= ai

        if p == x:
            return 1
        return 0
    
    count = 0
    
    for i in range(size[j]):
        arr.append(a[j][i])
        count += dfs(arr, j + 1)
        arr.pop()

    return count
    
print(dfs([], 0))
