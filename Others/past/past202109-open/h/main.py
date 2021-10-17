# -*- coding: utf-8 -*-


def dfs(cur_v, parent, x, graph):
    if x == 0:
        print("Yes")
        exit()
    
    for cost, next_v in graph[cur_v]:
        if next_v == parent:
            continue

        dfs(next_v, cur_v, x - cost, graph)
    

def main():
    import sys

    sys.setrecursionlimit(10 ** 7)
    input = sys.stdin.readline

    n, x = map(int, input().split())
    graph = [[] for _ in range(n)]
    
    for _ in range(n - 1):
        ai, bi, ci = map(int, input().split())
        ai -= 1
        bi -= 1
    
        graph[ai].append((ci, bi))
        graph[bi].append((ci, ai))
    
    for i in range(n):
        dfs(i, -1, x, graph)

    print("No")


if __name__ == "__main__":
    main()
