# -*- coding: utf-8 -*-


def main():
    s = input()[::-1]
    mod = 10 ** 9 + 7

    # DPテーブル（あまりが0～12となる組み合わせを管理）を用意
    n = 13
    dp = [0 for _ in range(n)]
    dp[0] = 1

    # 桁数の初期化
    digit = 1

    # 1文字ずつ見る
    for si in s:
        # 更新用のテーブルnext_dp[n]を用意
        next_dp = [0 for _ in range(n)]

        if si == '?':
            # '?'の取りうる範囲
            for q in range(10):
                # XXX: next_dpの括弧内の理解がかなり怪しい
                # digit - 1桁のときの結果を使って，
                # それぞれのあまりについて組み合わせの数を更新
                for j in range(n):
                    next_dp[(q * digit + j) % n] += dp[j]
                    next_dp[(q * digit + j) % n] %= mod
        else:
            q = int(si)

            for j in range(n):
                next_dp[(q * digit + j) % n] += dp[j]
                next_dp[(q * digit + j) % n] %= mod

        # DPテーブルを上書き
        dp = next_dp

        # 桁数を1つ増やす
        digit *= 10
        digit %= n

    # dp[5]が答え
    print(dp[5])


if __name__ == '__main__':
    main()
