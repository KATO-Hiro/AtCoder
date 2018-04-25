'''input
6 5
1 2
2 3
3 4
4 5
5 6
5

7 7
1 3
2 7
3 4
4 5
4 6
5 6
6 7
4

3 3
1 2
1 3
2 3
0

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem C


def dfs(x: int):
    if visited[x]:
        return

    visited[x] = True

    for i in range(n):
        if graph[x][i]:
            dfs(i)


if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    a = [0 for _ in range(m)]
    b = [0 for _ in range(m)]
    graph = [[0 for i in range(n)] for j in range(n)]

    # See:
    # https://img.atcoder.jp/abc075/editorial.pdf
    # https://www.youtube.com/watch?v=VJntQuR2zNI
    for i in range(m):
        line = list(map(int, input().split()))
        a[i] = line[0] - 1
        b[i] = line[1] - 1
        graph[a[i]][b[i]] = True
        graph[b[i]][a[i]] = True

    bridge_count = 0

    for j in range(m):
        graph[a[j]][b[j]] = False
        graph[b[j]][a[j]] = False

        visited = [False] * len(graph[0])
        dfs(0)

        if False in visited:
            bridge_count += 1

        graph[a[j]][b[j]] = True
        graph[b[j]][a[j]] = True

    print(bridge_count)
