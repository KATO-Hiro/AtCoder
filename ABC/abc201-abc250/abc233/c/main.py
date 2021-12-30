# -*- coding: utf-8 -*-


import sys
sys.setrecursionlimit(10 ** 7)

input = sys.stdin.readline

n, x = map(int, input().split())
a = [[] for _ in range(n)]
size = [0 for _ in range(n)]

for i in range(n):
    b = list(map(int, input().split()))
    l, ai = b[0], b[1:]
    size[i], a[i] = l, ai

ans = 0

def dfs(arr, j):
    global ans

    if len(arr) == n:
        p = 1

        for ai in arr:
            p *= ai

        if p == x:
            ans += 1
        return
    
    for i in range(size[j]):
        arr.append(a[j][i])
        dfs(arr, j + 1)
        arr.pop()
    
dfs([], 0)
print(ans)
