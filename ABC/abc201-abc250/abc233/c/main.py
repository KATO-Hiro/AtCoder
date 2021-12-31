# -*- coding: utf-8 -*-


from itertools import product
import sys

input = sys.stdin.readline

n, x = map(int, input().split())
a = [[] for _ in range(n)]

for i in range(n):
    _, *ai = map(int, input().split())
    a[i] = ai

ans = 0

for p in product(*a):
    mul = 1

    for pi in p:
        mul *= pi
    
    if mul == x:
        ans += 1

print(ans)
