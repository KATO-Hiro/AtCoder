# -*- coding: utf-8 -*-


def main():
    import sys
    sys.setrecursionlimit(10 ** 7)

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

    def dfs(vertex):
        visited[vertex] = True

        for to in graph[vertex]:
            if visited[to]:
                continue

            dfs(to)

    dfs(0)

    if False in visited:
        print("The graph is not connected.")
    else:
        print("The graph is connected.")


if __name__ == "__main__":
    main()
