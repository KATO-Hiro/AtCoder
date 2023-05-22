# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import deque

    input = sys.stdin.readline

    n, m = map(int, input().split())

    graph = [[] for _ in range(n + m)]

    # 超頂点: 集合とそれらを構成する頂点を一つのグラフとみなす
    # 操作回数の最小化を最短経路問題に帰着
    for i in range(n):
        _ = int(input())
        si = list(map(int, input().split()))

        for sij in si:
            sij -= 1
            graph[sij].append(m + i)
            graph[m + i].append(sij)

    # BFS
    q = deque([0])
    inf = 10**12
    dist = [inf] * (n + m)
    dist[0] = 0

    while q:
        qi = q.popleft()

        for to in graph[qi]:
            if dist[to] != inf:
                continue

            dist[to] = dist[qi] + 1
            q.append(to)

    ans = dist[m - 1]

    if ans == inf:
        ans = -1
    else:
        ans = (ans - 2) // 2  # 問題文の操作1回 = グラフの移動距離2 + 端部?の処理

    print(ans)


if __name__ == "__main__":
    main()
