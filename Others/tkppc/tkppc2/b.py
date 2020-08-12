# -*- coding: utf-8 -*-


def main():
    n, m = map(int, input().split())
    v = [0 for _ in range(n)]
    t = [0 for _ in range(n)]
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    for i in range(n):
        vi, ti = map(int, input().split())
        v[i] = vi
        t[i] = ti

    # 典型的なDP問題
    # dp[j][i]: j個目の書類を書き換えたときに、時間iにおける書類の重要度の合計の最大値
    for j in range(1, n + 1):
        for i in range(1, m + 1):
            # j - 1個目の書類を書き換えたときの最大値
            dp[j][i] = dp[j - 1][i]

            # j個目の作業を時間内に行うことができる場合
            # tとvは0-indexであることに注意
            remain = i - t[j - 1]

            if remain >= 0:
                # j個目の作業に必要な時間を除外したときの書類の重要度の最大値
                # + j個目の作業によって得られる書類の重要度
                dp[j][i] = max(dp[j][i], dp[j - 1][remain] + v[j - 1])

    # n行m列の値が答え
    print(dp[n][m])


if __name__ == '__main__':
    main()
