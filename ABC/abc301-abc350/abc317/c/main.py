# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    pending = -1
    dist = [[pending for _ in range(n)] for _ in range(n)]

    for _ in range(m):
        ai, bi, ci = map(int, input().split())
        ai -= 1
        bi -= 1

        dist[ai][bi] = ci
        dist[bi][ai] = ci

    # print(dist)

    # dp[s][v]: 訪問済みの頂点集合s、現在の頂点vとしたときの距離の最大値
    inf = -(10**18)
    dp = [[inf for _ in range(n)] for _ in range(1 << n)]

    # 初期化: 頂点iを始点としたときの距離を0に
    for i in range(n):
        dp[1 << i][i] = 0

    for s in range(1 << n):
        for v in range(n):
            if dp[s][v] == inf:
                continue

            for u in range(n):
                # 未訪問 + 到達不可能な場合を除外
                if not ((s >> u) & 1) and dist[v][u] != pending:
                    dp[s | 1 << u][u] = max(dp[s | 1 << u][u], dp[s][v] + dist[v][u])

    # 2次元のリストに対して、max(dp)とすると正しい答えが得られない
    ans = max([max(dp_i) for dp_i in dp])
    print(ans)


if __name__ == "__main__":
    main()
