# -*- coding: utf-8 -*-


def main():
    from collections import deque

    n, q = map(int, input().split())
    graph = [[] for _ in range(n)]

    # KeyInsight
    # 直線のグラフとみなす
    # 累積和の考え方を応用

    # 隣接リストを作成
    for i in range(n - 1):
        ai, bi = map(int, input().split())
        graph[ai - 1].append(bi - 1)
        graph[bi - 1].append(ai - 1)

    values = [0 for _ in range(n)]

    for j in range(q):
        pi, xi = map(int, input().split())
        values[pi - 1] += xi

    # 木の持ち方
    d = deque()
    d.append(0)
    visited = [False for _ in range(n)]
    visited[0] = True

    # bfs
    while d:
        di = d.popleft()

        for g in graph[di]:
            if not visited[g]:
                visited[g] = True
                values[g] += values[di]
                d.append(g)

    print(' '.join(map(str, values)))


if __name__ == '__main__':
    main()
