# -*- coding: utf-8 -*-


def main():
    # from sys import setrecursionlimit

    # setrecursionlimit(2 * 10 ** 6)

    n = int(input())
    b = [int(input()) for _ in range(n - 1)]
    sub = [[] for _ in range(n)]

    # ある上司から見たときの，直属の部下のリスト
    for index, bi in enumerate(b, 1):
        sub[bi - 1].append(index)

    # See:
    # https://atcoder.jp/contests/abc026/submissions/7059789
    pay = [0 for _ in range(n)]

    # 再帰関数
    def dfs(x):
        # 基本ケース：部下がいないときは1を返す
        if len(sub[x]) == 0:
            pay[x] = 1
            return pay[x]

        # 給料の最大値と最小値を初期化
        min_p = float('inf')
        max_p = 0

        # 直属の部下のリストを見る
        for s in sub[x]:
            # 再帰ケース
            dfs(s)
            # 最小値と最大値を更新
            max_p = max(max_p, pay[s])
            min_p = min(min_p, pay[s])

        pay[x] = max_p + min_p + 1
        return pay[x]

    print(dfs(0))


if __name__ == '__main__':
    main()
