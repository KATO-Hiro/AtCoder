# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import deque

    input = sys.stdin.readline

    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    graph = [[] for _ in range(n)]

    for i in range(n - 1):
        ai, bi = map(int, input().split())
        ai -= 1
        bi -= 1

        # 頂点番号 + 辺のidもセットで保持
        graph[ai].append((bi, i))
        graph[bi].append((ai, i))

    # 前計算: 与えられた経路でそれぞれ辺を何回通るか
    count = [0] * (n - 1)

    # See:
    # https://atcoder.jp/contests/abc222/submissions/26452884
    def bfs(start):
        inf = -1
        dist = [inf] * n
        dist[start] = 0
        q = deque([start])

        while q:
            qi = q.popleft()

            for to, _ in graph[qi]:
                if dist[to] != inf:
                    continue

                dist[to] = dist[qi] + 1
                q.append(to)

        return dist

    for start, goal in zip(a, a[1:]):
        start -= 1
        goal -= 1

        dist = bfs(start)
        cur = goal

        # 終点から始点までの経路をたどり、通過する辺を数える
        while cur != start:
            for to, edge_id in graph[cur]:
                if dist[to] < dist[cur]:
                    cur = to
                    count[edge_id] += 1

                    break

    # 合計S回のうち、赤い辺を何回通るか?
    # R - B = K、R + B = Sから、変数Bを削除
    r = k + sum(count)

    if r < 0 or r % 2 == 1:
        print(0)
        exit()

    # 赤い辺をいくつか選んで、合計r回にできるか?
    r //= 2
    dp = [0] * (r + 1)
    dp[0] = 1
    mod = 998244353

    for ci in count:
        for i in range(r - ci, -1, -1):
            dp[i + ci] += dp[i]
            dp[i + ci] %= mod

    print(dp[r])


if __name__ == "__main__":
    main()
