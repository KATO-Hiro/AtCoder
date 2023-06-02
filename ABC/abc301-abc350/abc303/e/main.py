# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import deque

    input = sys.stdin.readline

    n = int(input())
    graph = [[] for _ in range(n)]

    for _ in range(n - 1):
        ai, bi = map(int, input().split())
        ai -= 1
        bi -= 1

        graph[ai].append(bi)
        graph[bi].append(ai)

    # 葉に着目すると見通しが良くなる
    # 葉の隣がスターグラフの中心 + 隣接する頂点との関係を見る
    # 任意の葉を根とした頂点からの距離がmod 3 = 1のときにスターグラフの中心

    # 葉を探す = 隣接する頂点の数が1
    leaf = -1

    for i in range(n):
        if len(graph[i]) == 1:
            leaf = i
            break

    q = deque([leaf])
    inf = 10**12
    dist = [inf] * n
    dist[leaf] = 0
    ans = list()

    while q:
        cur = q.popleft()

        for to in graph[cur]:
            if dist[to] != inf:
                continue

            dist[to] = dist[cur] + 1
            q.append(to)

            if dist[to] % 3 == 1:
                ans.append(len(graph[to]))

    print(*sorted(ans))


if __name__ == "__main__":
    main()
