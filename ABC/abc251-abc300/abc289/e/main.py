# -*- coding: utf-8 -*-


from collections import deque


def solve():
    n, m = map(int, input().split())
    colors = list(map(int, input().split()))
    graph = [[] for _ in range(n)]
    
    for _ in range(m):
        ai, bi = map(int, input().split())
        ai -= 1
        bi -= 1
    
        graph[ai].append(bi)
        graph[bi].append(ai)
    
    # (高橋君のいる頂点ti、青木君のいる頂点ai)を状態とする最短経路問題に言い換え
    # 状態数O(n ** 2)、遷移: O(m ** 2)
    q = deque()
    inf = 10 ** 12
    dist = [[inf for _ in range(n)] for _ in range(n)]

    def push(i, j, d):
        if dist[i][j] != inf:
            return
        
        dist[i][j] = d
        q.append((i, j))
    
    push(0, n - 1, 0)

    while q:
        a, b = q.popleft()
        di = dist[a][b]

        for na in graph[a]:
            for nb in graph[b]:
                if colors[na] == colors[nb]:
                    continue

                push(na, nb, di + 1)
    
    ans = dist[n - 1][0]

    if ans == inf:
        ans = -1
    
    print(ans)


def main():
    import sys

    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
