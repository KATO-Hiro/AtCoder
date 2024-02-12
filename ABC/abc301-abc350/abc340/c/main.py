# -*- coding: utf-8 -*-

import sys
from functools import cache

sys.setrecursionlimit(10**8)

input = sys.stdin.readline

n = int(input())


# f(x): 整数xを1にするために必要なコスト
@cache
def rec(x):
    if x == 1:
        return 0
    else:
        return rec(x // 2) + rec(((x + 1) // 2)) + x


print(rec(n))
