# -*- coding: utf-8 -*-


def main():
    h, w = map(int, input().split())
    a = [list(input()) for _ in range(h)]
    dp = [[0 for _ in range(w)] for _ in range(h)]
    mod = 10 ** 9 + 7

    # See:
    # https://qiita.com/drken/items/03c7db44ccd27820ea0d#h-%E5%95%8F%E9%A1%8C---grid-1
    # ◯：自力で気がつけた点
    # △：自力で気がつけなかった点/解説を読めば理解できた点
    # ×：解説を読んでも理解できていない点

    # ◯経路のパターン数を管理
    # △2次元の配列で管理
    # ◯初期値は1通り
    dp[0][0] = 1

    for i in range(h):
        for j in range(w):
            # 配るDP
            # △数え上げDPでは，dp[to] += dp[from]が基本形
            # 次に進むマスがグリッドの範囲内，かつ，進むことができる
            if (j + 1 < w) and (a[i][j + 1] == '.'):
                dp[i][j + 1] += dp[i][j]
                dp[i][j + 1] %= mod

            if (i + 1 < h) and (a[i + 1][j] == '.'):
                dp[i + 1][j] += dp[i][j]
                dp[i + 1][j] %= mod

    # △求めるべき経路数
    print(dp[h - 1][w - 1])


if __name__ == '__main__':
    main()
