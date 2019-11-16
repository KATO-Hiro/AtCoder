# -*- coding: utf-8 -*-


def main():
    # See:
    # https://www.youtube.com/watch?v=VSeggcnxwrc

    # KeyInsight
    # L, Rでまとめる
    # 1回の操作で幸福度が最大で2増える
    # 操作したときの内部のスコアが変化しない
    # 例外的に，すべて同じ文字の場合は変化せず，ランレングス圧縮したときに2グループのときは1増える
    # min(理論値n - 1, 初期スコア + 2 * k回)

    # つまづきポイント
    # 反転操作で，スコアが変化する/変化しない部分を明らかにする
    # 操作が1回の場合を考えて，多数回に展開
    # スコアを増やす=異なるグループを減らす

    # どうしたら気がつけそうか?
    # 同じ要素をまとめる
    # 操作を言い換える，同じことを違う言葉で表現する/異なる視点で見る
    # 理論値VS初期値 + 操作による変化を比べる

    n, k = map(int, input().split())
    s = input()
    score = 0

    for i in range(n - 1):
        if s[i] == s[i + 1]:
            score += 1

    print(min(n - 1, score + 2 * k))


if __name__ == '__main__':
    main()
