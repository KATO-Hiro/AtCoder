# -*- coding: utf-8 -*-


def main():
    import sys

    sys.setrecursionlimit(10**8)

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

    def dfs(cur, parent=-1):
        if cur == goal:
            return True

        for to, edge_id in graph[cur]:
            if to == parent:
                continue

            if dfs(to, cur):
                count[edge_id] += 1

                return True

        return False

    for start, goal in zip(a, a[1:]):
        start -= 1
        goal -= 1
        dfs(start)

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
