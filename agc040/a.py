# -*- coding: utf-8 -*-


def main():
    s = list(input())
    n = len(s) + 1
    ans = [0 for _ in range(n)]

    # See:
    # https://www.youtube.com/watch?v=qIzuNgDV6O8
    # KeyInsight:
    # 不等号を一つずつ扱い，全探索で処理
    # <: a[i + 1] = max(a[i + 1], a[i] + 1)
    # >: a[i - 1] = max(a[i - 1], a[i] + 1)

    # 考察できた部分
    # 0で初期化
    # 愚直にサンプルからシミュレーション

    # 考察できなかった部分
    # 各項の値をどうプログラムで求めるか

    # ギャップ
    # 符号をまとめて処理しようとした
    # 途中で，符号の組み合わせによって，カウントを調整必要があることに気がついたが，法則性が分からず
    for i in range(n - 1):
        if s[i] == '<':
            ans[i + 1] = max(ans[i + 1], ans[i] + 1)

    for i in range(n - 2, -1, -1):
        if s[i] == '>':
            ans[i] = max(ans[i], ans[i + 1] + 1)

    print(sum(ans))


if __name__ == '__main__':
    main()
