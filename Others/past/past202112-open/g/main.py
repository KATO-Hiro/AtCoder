# -*- coding: utf-8 -*-


def bfs(n, graph, u, v):
    from collections import deque

    visited = [False for _ in range(n)]
    d = deque()
    d.append(u)

    while d:
        di = d.popleft()

        if visited[v]:
            return True

        if visited[di]:
            continue

        visited[di] = True

        for index, to in enumerate(graph[di]):
            if to == 1:
                d.append(index)
    
    return False


def main():
    import sys

    input = sys.stdin.readline

    n, q = map(int, input().split())
    graph = [[0] * n for _ in range(n)]

    for i in range(q):
        case, u, v = map(int, input().split())
        u -= 1
        v -= 1

        if case == 1:
            graph[u][v] ^= 1
            graph[v][u] ^= 1
        else:
            if bfs(n, graph, u, v):
                print("Yes")
            else:
                print("No")


if __name__ == "__main__":
    main()
