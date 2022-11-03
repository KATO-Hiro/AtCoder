# -*- coding: utf-8 -*-

ans = 0


from math import floor
from collections import defaultdict
import sys

input = sys.stdin.readline

n = int(input())
memo = defaultdict(int)

def dfs(i):
    global ans

    if i == 0:
        memo[i] = 1
        return 1
    
    if i in memo.keys():
        return memo[i]

    memo[i] = dfs(floor(i / 2)) + dfs(floor(i / 3))
    
    return memo[i]

dfs(n)
print(memo[n])
