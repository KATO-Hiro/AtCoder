# -*- coding: utf-8 -*-


def bfs(vertex_count: int, source: int, graph):
    from collections import deque

    d = deque()
    d.append(source)
    visited = [False] * vertex_count
    inf = 10 ** 18
    dist = [inf] * vertex_count
    dist[source] = 0

    while d:
        cur = d.popleft()

        if visited[cur]:
            continue

        visited[cur] = True

        for to in graph[cur]:
            if visited[to]:
                continue

            dist[to] = min(dist[to], dist[cur] + 1)
            d.append(to)

    return dist


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    
    for _ in range(m):
        ai, bi = map(int, input().split())
        ai -= 1
        bi -= 1
    
        # cost, vertex
        graph[ai].append(bi)
        graph[bi].append(ai)
    
    # 頂点piからの距離がdi未満の頂点を白で塗る 
    # 上記以外を黒で塗る(全て白ならNo)
    k = int(input())
    dist = list()
    pd = list()

    none, white, black = -1, 0, 1
    colors = [none] * n

    for _ in range(k):
        pi, di = map(int, input().split())
        pi -= 1

        # 前処理: 各頂点からの最短距離をBFSで求める
        d = bfs(vertex_count=n, source=pi, graph=graph)
        dist.append(d)
        pd.append((pi, di))
    
        for j, dij in enumerate(d):
            if dij < di:
                colors[j] = white
    
    count = 0

    for i, color in enumerate(colors):
        if color == none:
            colors[i] = black
            count += 1
    
    if count == 0:
        print("No")
        exit()
    
    inf = 10 ** 18
    
    # 頂点piと「黒で塗られた頂点のうち、頂点piとの距離の最小値」の距離がdiであるか判定
    for i, (pi, di) in enumerate(pd):
        d_min = inf

        for j, (color, dij) in enumerate(zip(colors, dist[i])):
            if color == black:
                d_min = min(d_min, dij)

        if d_min != di:
            print("No")
            exit()

    print("Yes")
    print(''.join(map(str, colors)))


if __name__ == "__main__":
    main()
