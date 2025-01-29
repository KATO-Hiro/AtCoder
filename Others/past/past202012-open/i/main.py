# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import deque

    input = sys.stdin.readline

    n, m, k = map(int, input().split())
    h = list(map(int, input().split()))
    c = list(map(int, input().split()))
    graph = [[] for _ in range(n)]

    for _ in range(m):
        ai, bi = map(int, input().split())
        ai -= 1
        bi -= 1

        # 逆向きに辺を貼る
        if h[ai] > h[bi]:
            graph[bi].append(ai)
        else:
            graph[ai].append(bi)

    inf = -1

    # 避難所を起点に多始点BFS
    d = deque()
    dist = [inf] * n

    for ci in c:
        ci -= 1
        d.append(ci)
        dist[ci] = 0

    while d:
        cur = d.popleft()

        for to in graph[cur]:
            if dist[to] != inf:
                continue

            d.append(to)
            dist[to] = dist[cur] + 1

    print(*dist, sep="\n")


if __name__ == "__main__":
    main()
