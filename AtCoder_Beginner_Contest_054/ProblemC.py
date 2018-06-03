'''input
3 3
1 2
1 3
2 3
2

4 5
1 2
2 3
3 4
1 3
2 4

7 7
1 3
2 7
3 4
4 5
4 6
5 6
6 7
1

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem C


# See:
# https://atcoder.jp/img/abc054/editorial.pdf
def dfs(v):
    all_visited = True

    if False in visited:
        all_visited = False

    if all_visited:
        return 1

    count = 0

    for i in range(n):
        if graph[v][i] == 0:
            continue

        if visited[i]:
            continue

        visited[i] = True
        count += dfs(i)
        visited[i] = False
    return count


if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    graph = [[0 for __ in range(n)] for _ in range(n)]

    for i in range(m):
        a, b = list(map(lambda x: int(x) - 1, input().split()))
        graph[a][b] = 1
        graph[b][a] = 1

    visited = [False] * n
    visited[0] = True

    print(dfs(0))
