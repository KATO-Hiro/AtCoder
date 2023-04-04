# -*- coding: utf-8 -*-

ans = 0


def main():
    import sys
    sys.setrecursionlimit(10 ** 8)

    input = sys.stdin.readline

    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    
    for _ in range(m):
        ai, bi = map(int, input().split())
        ai -= 1
        bi -= 1
    
        graph[ai].append(bi)
        graph[bi].append(ai)
    
    visited = [False] * n
    upper = 10 ** 6

    def dfs(vertex):
        global ans

        if ans == upper:
            return
        
        visited[vertex] = True
        ans += 1

        for to in graph[vertex]:
            if visited[to]:
                continue
        
            dfs(to)
    
        visited[vertex] = False

    dfs(0)
    print(ans)


if __name__ == "__main__":
    main()
