# -*- coding: utf-8 -*-


import sys
sys.setrecursionlimit(10 ** 7)

input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n)]

for _ in range(n - 1):
    ai, bi = map(int, input().split())
    ai -= 1
    bi -= 1

    graph[ai].append(bi)
    graph[bi].append(ai)

left = [-1] * n
right = [-1] * n
leaf_count = 1

# 木のDFS
def dfs(vertex, parent=-1):
    global leaf_count
    left[vertex] = leaf_count

    for to in graph[vertex]:
        if to == parent:
            continue

        dfs(to, vertex)
    
    # 葉の判定
    # 次数が1 & 親ではない
    if len(graph[vertex]) == 1 and parent != -1:
        leaf_count += 1

    right[vertex] = leaf_count - 1

dfs(0)

for li, ri in zip(left, right):
    print(li, ri)

