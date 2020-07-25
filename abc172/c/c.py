# -*- coding: utf-8 -*-


def main():
    import sys
    input = sys.stdin.readline

    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    # KeyInsight:
    # ◯: 配列の要素の合計を前計算しておく
    # △: 尺取り法に気がつけなかった。
    # △: 解説動画を見て自分で実装したら、サンプルのインデックスエラーが消えずに詰んだ。
    # See:
    # https://www.youtube.com/watch?v=v8ppNGf49Nk&feature=youtu.be
    time = 0

    for bi in b:
        time += bi

    j = m
    ans = 0

    for i in range(n + 1):
        # bの要素を選択できる、かつ、kより所要時間が長いときに、本を減らす
        while (j > 0 and time > k):
            j -= 1
            time -= b[j]

        # 全てのbの要素を除外したケースへの対応
        if time > k:
            break

        # aとbの要素数と、これまでの最大値とを比較
        ans = max(ans, i + j)

        # 実装上の工夫:
        # 配列参照外を防ぐ
        if (i == n):
            break

        # 実装上の工夫:
        # aの要素を次のループの前に計算しておく
        time += a[i]

    print(ans)


if __name__ == '__main__':
    main()
