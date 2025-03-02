# -*- coding: utf-8 -*-


def main():
    import sys
    from heapq import heappop, heappush

    input = sys.stdin.readline

    n, m, x = map(int, input().split())
    n *= 2
    graph = [[] for _ in range(n)]

    # 頂点倍加
    # 頂点と flip の有無のペアを頂点としたグラフを作る
    for _ in range(m):
        ai, bi = map(int, input().split())
        ai -= 1
        bi -= 1

        graph[ai * 2].append(bi * 2)
        graph[bi * 2 + 1].append(ai * 2 + 1)

    inf = 10**18
    dist = [inf] * n
    hq = []  # 距離、頂点

    def push(vertex, d):
        if dist[vertex] <= d:
            return

        dist[vertex] = d
        heappush(hq, (d, vertex))

    push(0, 0)

    while hq:
        di, cur = heappop(hq)

        if dist[cur] == inf:
            continue

        for to in graph[cur]:
            push(to, di + 1)

        # flip した場合の頂点への遷移
        push(cur ^ 1, di + x)

    ans = min(dist[-1], dist[-2])
    print(ans)


if __name__ == "__main__":
    main()
