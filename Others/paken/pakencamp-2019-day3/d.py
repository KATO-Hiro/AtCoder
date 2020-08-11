# -*- coding: utf-8 -*-


def main():
    n = int(input())
    s = [list(input()) for _ in range(5)]
    rbw = [[0 for _ in range(n)] for _ in range(3)]

    # 前処理：各列で赤，青，白と決め打ったときに何回塗り替える必要があるか
    for i in range(n):
        r_count = 5
        b_count = 5
        w_count = 5

        for j in range(5):
            if s[j][i] == 'R':
                r_count -= 1
            elif s[j][i] == 'B':
                b_count -= 1
            elif s[j][i] == 'W':
                w_count -= 1

        rbw[0][i] = r_count
        rbw[1][i] = b_count
        rbw[2][i] = w_count

    # See:
    # https://img.atcoder.jp/pakencamp-2019-day3/editorial-d.pdf
    # 愚直に計算すると3 * 2 ^ (n - 1)通りある
    # 動的計画法を使う
    # 操作回数が直前の状態にのみ依存しているため
    # dp[j][i]：ある列iで，色jを選択したときに必要なマスの書き換え回数
    dp = [[float('inf') for _ in range(n + 1)] for _ in range(3)]

    # 初期化
    dp[0][0] = 0
    dp[1][0] = 0
    dp[2][0] = 0

    for i in range(1, n + 1):
        for j in range(3):
            for k in range(3):
                if j == k:
                    continue

                # ある列iのすぐ左の列から，重複しない色を選ぶ
                # ある列で色jとしたときに必要な書き換え回数
                dp[j][i] = min(dp[j][i], dp[k][i - 1] + rbw[j][i - 1])

    # 列nの最小値が答え
    print(min(dp[0][-1], dp[1][-1], dp[2][-1]))


if __name__ == '__main__':
    main()
