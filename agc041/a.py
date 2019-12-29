# -*- coding: utf-8 -*-


def main():
    n, a, b = map(int, input().split())
    diff = b - a

    # See:
    # https://img.atcoder.jp/agc041/editorial.pdf
    # KeyInsight: 移動パターンを分解する

    # ◯：A, Bの位置の偶奇が一致しているかどうかの場合分け
    #   ：A, Bの位置の偶奇が不一致のときに，片方が端部まで移動する
    # ×：上記のcaseでの最短roundを計算する部分
    if diff % 2 == 0:
        print(diff // 2)
    else:
        # A, Bが端部に移動するまでの回数: min(a - 1, n - b)
        # 偶奇を調整する回数           : 1
        # AとBが合流するまでに必要な回数: (b - a - 1) // 2
        print(min(a - 1, n - b) + 1 + (b - a - 1) // 2)


if __name__ == '__main__':
    main()
