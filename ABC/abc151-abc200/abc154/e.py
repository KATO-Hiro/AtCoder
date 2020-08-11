# -*- coding: utf-8 -*-


def main():
    s = list(input())
    n = len(s)
    large_k = int(input())
    # KeyInsight: 桁DP
    # dp[i][j][k]
    # i桁目、j個の非0、k:そこまでの桁がNと一致する(0), N未満(1)
    ## i, kは典型的な状態、jに気が付けるかどうか
    # See:
    # http://hiroto1979.hatenablog.jp/entry/2016/03/18/224631
    dp = [[[0 for k in range(2)] for j in range(4)] for i in range(105)]
    ## なぜ初期値が1になる?
    dp[0][0][0] = 1

    # See:
    # https://www.youtube.com/watch?v=JQmQjJd-sLA&feature=youtu.be
    # http://drken1215.hatenablog.com/entry/2019/02/04/013700
    # https://torus711.hatenablog.com/entry/20150423/1429794075
    for i in range(n):
        for j in range(4):
            for k in range(2):
                # 次の桁の数字
                nd = int(s[i])

                # 各桁で0〜9を試す
                for digit in range(10):
                    ni, nj, nk = i + 1, j, k

                    # 遷移ができるかどうかを判定
                    ## 遷移できない条件を列挙して、計算をしないようにする
                    # ある桁で、0以外の数字を使う
                    if digit != 0:
                        nj += 1

                    # 0でない数字がK個より大きいときは、遷移しない
                    if nj > large_k:
                        continue

                    # ある桁まで見たときに、Nと一致する
                    if k == 0:
                        # ある桁の数字より大きいときは、遷移しない
                        if digit > nd:
                            continue
                        # 小さいときは、Nと一致しない(=それ以降の桁にはどんな数字を入れてもよい)
                        elif digit < nd:
                            nk = 1

                    dp[ni][nj][nk] += dp[i][j][k]

    # N未満とNの合計
    print(dp[n][large_k][0] + dp[n][large_k][1])


if __name__ == '__main__':
    main()
