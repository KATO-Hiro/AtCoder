# -*- coding: utf-8 -*-


def dijkstra(vertex_count: int, source: int, edges):
    """Uses Dijkstra's algorithm to find the shortest path in a graph.
    Args:
        vertex_count: The number of vertices.
        source      : Vertex number (0-indexed).
        edges       : List of (cost, edge) (0-indexed).
    Returns:
        costs  : List of the shortest distance.
        parents: List of parent vertices.
    Landau notation: O(|Edges|log|Vertices|).
    See:
    https://atcoder.jp/contests/abc191/submissions/19964078
    https://atcoder.jp/contests/abc191/submissions/19966232
    """

    from heapq import heappop, heappush

    hq = [(0, source)]  # weight, vertex number (0-indexed)
    costs = [float("inf") for _ in range(vertex_count)]
    costs[source] = 0
    visited = [False for _ in range(vertex_count)]
    pending = -1
    parents = [pending for _ in range(vertex_count)]

    while hq:
        cost, vertex = heappop(hq)

        if cost > costs[vertex]:
            continue

        if visited[vertex]:
            continue

        visited[vertex] = True

        for weight, edge in edges[vertex]:
            new_cost = cost + weight

            if new_cost < costs[edge]:
                costs[edge] = new_cost
                parents[edge] = vertex
                heappush(hq, (new_cost, edge))

    return costs, parents


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
        graph[ai].append((1, bi))
        graph[bi].append((1, ai))
    
    # 前処理: 各頂点からの最短距離をBFSで求める
    dist = list()

    for i in range(n):
        d, _ = dijkstra(vertex_count=n, source=i, edges=graph)
        dist.append(d)

    # 頂点piからの距離がdi未満の頂点を白で塗る 
    # 上記以外を黒で塗る(全て白ならNo)
    k = int(input())
    pd = list()

    for _ in range(k):
        pi, di = map(int, input().split())
        pi -= 1
        pd.append((pi, di))
    
    none, white, black = -1, 0, 1
    colors = [none] * n
    
    for pi, di in pd:
        for j, dij in enumerate(dist[pi]):
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
    
    # 頂点piと「黒で塗られた頂点のうち、頂点piとの距離の最小値」の距離がdiであるか判定
    for pi, di in pd:
        d_min = float("inf")

        for j, dij in enumerate(dist[pi]):
            if colors[j] == white:
                continue

            d_min = min(d_min, dij)
        
        if d_min != di:
            print("No")
            exit()

    print("Yes")
    print(''.join(map(str, colors)))


if __name__ == "__main__":
    main()
