# -*- coding: utf-8 -*-


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
    
    visited = [False] * n
    path = list()
    
    def dfs(cur, parent=-1):
        visited[cur] = True
        path.append(cur + 1)

        for to in sorted(graph[cur]):
            if visited[to] or to == parent:
                continue

            dfs(to, cur)
            path.append(cur + 1)
        
    results = dfs(0)
    print(*path)


if __name__ == "__main__":
    main()
