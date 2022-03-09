# -*- coding: utf-8 -*-


leaf_count = 1


def main():
    import sys

    input = sys.stdin.readline
    sys.setrecursionlimit(10 ** 7)

    n = int(input())
    graph = [[] for _ in range(n)]
    
    for _ in range(n - 1):
        ai, bi = map(int, input().split())
        ai -= 1
        bi -= 1
    
        graph[ai].append(bi)
        graph[bi].append(ai)
    
    left = [1] * n
    right = [1] * n
    
    def dfs(cur, parent=-1):
        global leaf_count
        left[cur] = leaf_count

        for to in graph[cur]:
            if to == parent:
                continue
            
            dfs(to, cur)
        
        if len(graph[cur]) == 1 and parent != -1:
            leaf_count += 1

        right[cur] = leaf_count - 1

    dfs(0)

    for i in range(n):
        print(left[i], right[i])


if __name__ == "__main__":
    main()
