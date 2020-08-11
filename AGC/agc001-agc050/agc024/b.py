# -*- coding: utf-8 -*-


def main():
    n = int(input())

    # See:
    # https://www.youtube.com/watch?v=S1IkBhwnuYU
    # KeyInsight
    # 取り出した部分列が昇順かつ連続した数字が並んでいるかどうか

    # ■できた部分
    # N - 部分列の長さの最大値が答え

    # ■できなかった部分
    # 判定方法：
    # piの値が並び替え前にどこに位置しているかをメモ
    # 昇順かつ連続して並んでいる部分列の長さを数える
    p = [0 for _ in range(n)]

    # See:
    # https://atcoder.jp/contests/agc024/submissions/2532965
    for i in range(n):
        x = int(input())
        x -= 1
        p[x] = i

    len_max = 1
    count = 1

    for i in range(1, n):
        if p[i] > p[i - 1]:
            count += 1
        else:
            count = 1

        # WAが取れなかった原因：部分列の最大値の更新ができていない場合があった
        # 例：すべて昇順に並んでいる
        len_max = max(len_max, count)

    print(n - len_max)


if __name__ == '__main__':
    main()
