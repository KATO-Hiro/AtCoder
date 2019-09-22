# -*- coding: utf-8 -*-


def main():
    s = input()
    k = int(input())
    remain = k  # 残りの操作回数
    ans = ['' for _ in range(len(s))]

    # See:
    # http://code-festival-2016-quala.contest.atcoder.jp/data/other/code-festival-2016-quala/editorial.pdf
    # KeyInsight
    # 辞書順最小：先頭の要素から順に見て，見ている要素をできるだけ小さくする，ことを貪欲に行う
    for index, si in enumerate(s):
        # アルファベットを数字に変換して扱う
        need = (ord('z') - ord(si) + 1) % 26

        # 先頭から'a'にできるかどうか判定
        if remain >= need:
            remain -= need
            ans[index] = 'a'
        else:
            ans[index] = si

    # 最後に，一番右の文字に対して残ったk回(mod 26)の操作を実行
    # 操作回数kはは最大で10^9回であり，愚直に計算すると実行時間制限をオーバーしてしまう
    # そこで，操作とアルファベットの関係にに注目する
    # 26文字で1周するという性質から，x周(ここは無視できる)+α回操作すると言い換える
    # α回操作して，該当する文字を返す

    # See:
    # https://atcoder.jp/contests/code-festival-2016-quala/submissions/7337728
    if remain > 0:
        ans[-1] = chr(ord('a') + ((ord(s[-1]) - ord('a') + remain) % 26))

    print(''.join(map(str, ans)))


if __name__ == '__main__':
    main()
