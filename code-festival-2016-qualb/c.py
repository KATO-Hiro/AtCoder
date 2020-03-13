# -*- coding: utf-8 -*-


def main():
    import sys
    input = sys.stdin.readline

    w, h = map(int, input().split())
    pq = [None] * (w + h)

    # KeyInsight:
    # 全域最小木: 任意の2点を行き来できる&コストを最小化する問題
    # ◯: コストを昇順に並び替える
    # ×: 各コストが何本該当するか?
    for i in range(w + h):
        if i < w:
            pq[i] = (int(input()), 'x')
        else:
            pq[i] = (int(input()), 'y')

    x_count = w + 1
    y_count = h + 1
    ans = 0

    # 一つ道路を舗装すると、片方の座標の辺の数が一つ減る
    # abst: 連結成分を作ると、幅が一つ減る
    # 図のイメージは、以下のURLを参照
    # https://scrapbox.io/ganariya/AtCoderCODEFESTIVAL2016qualB_C%E5%95%8F%E9%A1%8C500%E7%82%B9_%E3%80%8CC_-_Gr-idian_MST%E3%80%8D
    for cost, flag in sorted(pq):
        if flag == 'x':
            ans += cost * y_count
            x_count -= 1
        else:
            ans += cost * x_count
            y_count -= 1

    print(ans)


if __name__ == '__main__':
    main()
