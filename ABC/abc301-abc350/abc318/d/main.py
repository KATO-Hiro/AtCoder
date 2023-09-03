# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    d = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    edges = list()

    for i in range(n):
        di = list(map(int, input().split()))

        for j, dij in enumerate(di):
            j += i + 1

            d[i][j] = dij
            d[j][i] = dij

            # 頂点の集合をシフト演算子で表現
            edges.append((1 << i | 1 << j, d[i][j]))

    dp = [0] * (1 << n)

    for bit in range(1 << n):
        for edge_pair, weight in edges:
            # 選んだ辺の端点が異なる = 頂点集合の共通部分がない
            if bit & edge_pair != 0:
                continue

            pos = bit | edge_pair
            dp[pos] = max(dp[pos], dp[bit] + weight)

    print(max(dp))


if __name__ == "__main__":
    main()
